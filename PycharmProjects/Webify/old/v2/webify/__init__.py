from functools import wraps, partial
from inspect import signature
from itertools import zip_longest
from types import FunctionType
from typing import Callable, Generic
from urllib.parse import parse_qs
from wsgiref.util import shift_path_info

from my_utils import RecursiveDefaultDict
from my_utils.functions import call_is_valid, constant
from my_utils.typing import wsgi
from .db import *
from .db import __all__ as _db_all

__all__ = ['Application'] + _db_all

KT = TypeVar('KT')
T = TypeVar('T')
VT = TypeVar('VT')
Managed_T = TypeVar('Managed_T', bound='Managed')


class Managed(Generic[T], ABC):
    @classmethod
    @abstractmethod
    def get_instances(cls: Type[Managed_T[T]]) -> Iterable[Managed_T[T]]:
        pass
    
    @classmethod
    @abstractmethod
    def get_instance_by_id(cls: Type[Managed_T[T]], identifier: T) -> Managed_T[T]:
        pass
    
    @property
    @abstractmethod
    def id(self: Managed_T[T]) -> T:
        pass
    
    @property
    @abstractmethod
    def all_fields(self: Managed_T[T]) -> Mapping[str, Any]:
        pass
    
    @property
    @abstractmethod
    def preview_fields(self: Managed_T[T]) -> Mapping[str, Any]:
        pass
    
    @abstractmethod
    def register(self: Managed_T[T]) -> None:
        pass


def apify_class(cls: Type[Managed]) -> RecursiveDefaultDict[str, wsgi.Callable]:
    routes: RecursiveDefaultDict[str, wsgi.Callable] = RecursiveDefaultDict()
    
    def add_route(path: Iterable[str], methods: List[str]):
        path = tuple(path)
        
        current_branch_start = routes
        
        for i, component in enumerate(path):
            if isinstance(component, str):
                current_branch_start = current_branch_start[component]
            else:
                remainder = path[i:]
        else:
            remainder = ()
        
        def decorator(f: wsgi.Callable) -> wsgi.Callable:
            previous = current_branch_start.get('')
            
            def g(environ: wsgi.Environ, start_response: wsgi.StartResponse) -> wsgi.Iterable:
                if environ['REQUEST_METHOD'].upper() in methods:
                    current_branch = current_branch_start
                    args = []
        
                    for expected, actual in zip_longest(remainder, iter(partial(shift_path_info, environ), '')):
                        if expected is None or actual is None:
                            break
            
                        if isinstance(remainder, str):
                            if expected == actual:
                                current_branch = current_branch[actual]
                            else:
                                break
                        else:
                            try:
                                value = expected(actual)
                            except Exception:
                                break
                            else:
                                args.append(value)
                    else:
                        # noinspection PyArgumentList
                        return f(*args, environ, start_response)
    
                if isinstance(previous, Callable):
                    return previous(environ, start_response)
                else:
                    start_response('405 Method Not Allowed', [])
                    return ()

            g.__name__ = '_'.join(path)

            current_branch_start[''] = g
            return f
        
        return decorator
    
    def prepend_class_to_name(f: FunctionType) -> FunctionType:
        f.__name__ = f'{cls.__name__}_{f.__name__}'
        return f
    
    @add_route([], ['GET'])
    @prepend_class_to_name
    def list_instances(environ: wsgi.Environ, start_response: wsgi.StartResponse) -> wsgi.Iterable:
        yield '\n'.join(x.preview_fields for x in cls.get_instances())
    
    @add_route([], ['POST'])
    @prepend_class_to_name
    def add_instance(environ: wsgi.Environ, start_response: wsgi.StartResponse) -> wsgi.Iterable:
        try:
            instance = cls(**dict(line.split('\t', 1) for line in environ['wsgi.input']))
        except TypeError:
            start_response('400 Bad Request', [])
        else:
            start_response('201 Created', [])
            instance.register()
        
        return ()
    
    @add_route([str], ['GET'])
    @prepend_class_to_name
    def get_instance_info(identifier: str, environ: wsgi.Environ, start_response: wsgi.StartResponse) -> wsgi.Iterable:
        yield '\n'.join(x.all_fields for x in cls.get_instance_by_id(identifier))
    
    return routes


def htmlify_class(cls: Type) -> RecursiveDefaultDict[str, wsgi.Callable]:
    pass


def apify_callable(f: Callable[..., Any]) -> RecursiveDefaultDict[str, wsgi.Callable]:
    @wraps(f)
    def g(environ: wsgi.Environ, start_response: wsgi.StartResponse) -> wsgi.Iterable:
        param_dict = parse_qs(environ.get('QUERY_STRING', ''))
        
        if call_is_valid(f, (), param_dict):
            start_response('200 OK', [])
            yield repr(f(**param_dict))
        else:
            start_response('400 Bad Request', [])
            yield repr(signature(f))
    
    return RecursiveDefaultDict({'': g})


def htmlify_callable(f: Callable[..., Any]) -> RecursiveDefaultDict[str, wsgi.Callable]:
    pass


class RecursiveMapping(Generic[KT, VT], Mapping[KT, Union[VT, 'RecursiveMapping[KT, VT]']], ABC):
    pass


def call_dict(routes: Union[wsgi.Callable, RecursiveMapping[str, wsgi.Callable]], environ: wsgi.Environ,
              start_response: wsgi.StartResponse) -> wsgi.Iterable:
    while True:
        if isinstance(routes, Callable):
            return routes(environ, start_response)
        
        path_component = shift_path_info(environ)
        
        if path_component in routes:
            routes = routes[path_component]
        elif '' in routes:
            return routes[''](environ, start_response)
        else:
            start_response('404 Not Found', [])
            return ()


class Application(wsgi.Callable):
    routes: RecursiveDefaultDict[str, wsgi.Callable]
    
    def __init_subclass__(cls, api_path: str = 'api', **kwargs: Any) -> None:
        cls.routes = RecursiveDefaultDict()
        
        for name, value in vars(cls).items():
            if not value.startswith('_'):
                if isinstance(value, type) and issubclass(value, Managed):
                    cls.routes[name].update(htmlify_class(value))
                    cls.routes[api_path][name].update(apify_class(value))
                elif isinstance(value, Callable):
                    cls.routes[name][''] = htmlify_callable(value)
                    cls.routes[api_path][name][''] = apify_callable(value)
                else:
                    cls.routes[name][''] = htmlify_callable(constant(value))
                    cls.routes[api_path][name][''] = apify_callable(constant(value))
    
    def __call__(self, environ: wsgi.Environ, start_response: wsgi.StartResponse) -> wsgi.Iterable:
        return call_dict(self.routes, environ, start_response)
