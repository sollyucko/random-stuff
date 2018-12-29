import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import partial, wraps
from inspect import signature
from operator import setitem
from typing import Any, Callable, Dict, Generic, Iterable, Tuple, Type, TypeVar, Union
from wsgiref.util import shift_path_info

from my_utils.functions import call_is_valid
from my_utils.typing import wsgi

T = TypeVar('T')
Managed_ = TypeVar('Managed_', bound='Managed')


class Node(wsgi.Callable):
    methods: Dict[str, wsgi.Callable]  # Methods should be stored as uppercase.
    subnodes: Dict[str, 'Node']
    subnode_patterns: Dict[Callable[[str], Any], 'Node']  # Requires preservation of insertion order.
    
    def __init__(self):
        self.methods = {}
        self.subnodes = {}
    
    def __getitem__(self, key: str) -> 'Node':
        try:
            return self.subnodes[key]
        except KeyError:
            for pattern, subnode in reversed(tuple(self.subnode_patterns.items())):  # The newest patterns have priority.
                # noinspection PyBroadException
                try:
                    pattern(key)
                except Exception:
                    pass
                else:
                    return subnode  # Always returns the node.
            else:
                return self.subnodes.setdefault(key, Node())  # Creats a new node if not found.
    
    def get(self, key: str) -> Union['Node', Tuple[Any, 'Node']]:
        try:
            return self.subnodes[key]
        except KeyError as ex:
            for pattern, subnode in reversed(tuple(self.subnode_patterns.items())):  # The newest patterns have priority.
                # noinspection PyBroadException
                try:
                    key_object = pattern(key)
                except Exception:
                    pass
                else:
                    return key_object, subnode  # Sometimes returns a (key_object, node) tuple.
            else:
                raise KeyError(f'Key not found in {self!r}') from ex  # Errors if not found.
    
    def __setitem__(self, key, value):
        if isinstance(key, str):
            self.subnodes[key] = value
        else:
            del self.subnode_patterns[key]  # Make sure to add to the end.
            self.subnode_patterns[key] = value
    
    def update(self, node: 'Node'):
        self.methods.update(node.methods)
        
        for key, subnode in node.subnodes.items():
            self.subnodes.setdefault(key, Node()).update(subnode)
        
        for pattern, subnode in node.subnode_patterns.items():
            self.subnode_patterns.setdefault(pattern, Node()).update(subnode)
    
    def __call__(self, environ: wsgi.Environ, start_response: wsgi.StartResponse, *args: Any) -> wsgi.Iterable:
        try:
            x = self.get(shift_path_info(environ))
            
            try:
                if isinstance(x, tuple):
                    f, arg = x
                    return f(environ, start_response, *args, arg)
                else:
                    return x(environ, start_response, *args)
            except HTTPStatus as ex:
                start_response(ex.status, ex.headers)
                return ex.info,
            except Exception as ex:
                logging.error(ex)
                start_response('500 Internal Error', [])
                return ()
        except IndexError:
            try:
                return self.methods[environ['REQUEST_METHOD']](environ, start_response, *args)
            except IndexError:
                if self.methods:
                    start_response('405 Method Not Allowed', ['Allow', ', '.join(self.methods)])
                else:
                    start_response('404 Not Found', [])


class Managed(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    def get(cls: Type[Managed_[T]], identifier: T) -> Managed_[T]:
        ...
    
    @classmethod
    @abstractmethod
    def get_instances(cls: Type[Managed_[T]]) -> Iterable[Managed_[T]]:
        ...
    
    @classmethod
    @abstractmethod
    def register_instance(cls: Type[Managed_[T]], instance: Managed_[T]) -> None:
        ...
    
    @property
    @abstractmethod
    def identifier(self: Managed_[T]) -> T:
        ...


@dataclass
class HTTPStatus(Exception):
    status: str
    info: str = ''
    headers: wsgi.ResponseHeaders = field(default_factory=list)


def parse_query_string(query_string):
    query = map(lambda x: x.split('='), query_string.split('&'))
    args = tuple(value for key, value in query if not key)
    kwargs = dict(query)
    return args, kwargs


def api_from_callable(f: Callable[..., Any]) -> Node:
    node: Node = Node()
    
    @partial(setitem, node.methods, 'GET')
    @wraps(f)
    def _(environ: wsgi.Environ, start_response: wsgi.StartResponse, *original_args: Any) -> wsgi.Iterable:
        try:
            args, kwargs = parse_query_string(environ['QUERY_STRING'])
        except ValueError:
            start_response('400 Bad Request', [])
            return ()
        
        del kwargs['']
        
        if call_is_valid(f, args, kwargs):
            return repr(f(*original_args, *args, **kwargs))
        else:
            start_response('400 Bad Request', [])
            return repr(signature(f)),
    
    return node


def api_from_class(cls: Managed) -> Node:
    try:
        identifier_argument_name: str = tuple(signature(cls.get).parameters)[0]
    except TypeError:
        identifier_argument_name: str = 'identifier'
    
    try:
        # noinspection PyUnresolvedReferences
        identifier_type: Callable[[str], Any] = cls.get.__annotations__[identifier_argument_name]
    except (KeyError, TypeError):
        identifier_type: Callable[[str], Any] = str
    
    node: Node = Node()
    
    @partial(setitem, node.methods, 'GET')
    @wraps(cls.get_instances)
    def _(environ: wsgi.Environ, start_response: wsgi.StartResponse, *args: Any) -> wsgi.Iterable:
        start_response('200 OK', [])
        
        for instance in cls.get_instances(*args):
            yield repr(instance)
            yield '\n'
    
    @partial(setitem, node.methods, 'POST')
    @wraps(cls.register_instance)
    def _(environ: wsgi.Environ, start_response: wsgi.StartResponse, *original_args: Any) -> wsgi.Iterable:
        try:
            args, kwargs = parse_query_string(environ['QUERY_STRING'])
            instance = cls(*original_args, *args, **kwargs)
        except ValueError:
            start_response('400 Bad Request', [])
            return ()
        
        cls.register_instance(instance)
        
        start_response('200 OK', [('Location', environ['SCRIPT_NAME'] + '/' + repr(instance.identifier))])
    
    @partial(setitem, node.subnode_patterns.setdefault(identifier_type, Node()).methods, 'GET')
    @wraps(cls.get)
    def _(environ: wsgi.Environ, start_response: wsgi.StartResponse, *args: Any) -> wsgi.Iterable:
        try:
            instance = cls.get(*args)
        except LookupError:
            start_response('404 Not Found', [])
            return ()
        else:
            start_response('200 OK', [])
            return repr(instance),
    
    return node
