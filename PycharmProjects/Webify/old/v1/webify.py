from operator import attrgetter
from typing import Callable, Dict, Generic, Iterable, Optional, Type, TypeVar
from wsgiref.headers import Headers
from wsgiref.util import shift_path_info

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import Session, sessionmaker

from my_utils.strings import buffered_join
from my_utils.typing import wsgi

Column_T = TypeVar('Column_T', bound=wsgi.Callable)
DeclarativeMeta_T = TypeVar('DeclarativeMeta_T', bound=DeclarativeMeta)
T = TypeVar('T')


class BranchEndpoint(wsgi.Callable):
    def __init__(self, endpoint_dict: Optional[Dict[str, wsgi.Callable]] = None):
        self.endpoint_dict = {} if endpoint_dict is None else endpoint_dict
    
    def __call__(self, environ: wsgi.Environ, start_response: wsgi.StartResponse) -> wsgi.Iterable:
        try:
            endpoint = self[shift_path_info(environ)]
        except KeyError:
            start_response('404 Not Found', [])
        else:
            return self[shift_path_info(environ)](environ, start_response)
    
    def __getitem__(self, index: str) -> wsgi.Callable:
        return self.endpoint_dict[index]
    
    def endpoint(self, name: str) -> Callable[[Column_T], Column_T]:
        def decorator(f: Column_T) -> Column_T:
            self.endpoint_dict[name] = f
            return f
        
        return decorator


class DBEndpoint(BranchEndpoint, Generic[DeclarativeMeta_T]):
    def __init__(self, table: Type[DeclarativeMeta_T], session_maker: sessionmaker):
        super().__init__()
        
        self.table = table
        self.session_maker = session_maker
    
    def create_instance(self, environ: wsgi.Environ) -> T:
        pass
    

class RestEndpoint(DBEndpoint[DeclarativeMeta_T]):
    def __init__(self, table: Type[DeclarativeMeta_T], session_maker: sessionmaker):
        super().__init__(table, session_maker)
        
        @self.endpoint('')
        def items(environ: wsgi.Environ, start_response: wsgi.StartResponse) -> wsgi.Iterable:
            method = environ['REQUEST_METHOD']
            session: Session = self.session_maker()
            
            if method == 'GET':
                start_response('200 OK', [])
                yield from buffered_join(map(attrgetter('id'), session.query(self.table).all()), '\n')
            elif method == 'POST':
                start_response('204 No Content', [])
                session.add(self.create_instance(environ))
                session.commit()
            else:
                start_response('405 Method Not Allowed', [])
    
    def __getitem__(self, index: str) -> wsgi.Callable:
        try:
            return super().__getitem__(index)
        except ValueError:
            def item(environ: wsgi.Environ, start_response: wsgi.StartResponse) -> wsgi.Iterable:
                method = environ['REQUEST_METHOD']
                session: Session = self.session_maker()
                
                if method == 'GET':
                    result = session.query(self.table).get(index)
                    
                    if result is None:
                        start_response('404 Not Found', [])
                    else:
                        start_response('200 OK', [])
                        yield repr(result)
                elif method == 'PATCH':
                    result = session.query(self.table).filter_by(id=index)
                    
                    if result.count():
                        start_response('404 Not Found')
                    else:
                        obj = result.first()
                        
                        for line in environ['wsgi.input']:
                            name, value = line.split()
                            setattr(obj, name, self.objectify(getattr(self.table, name), value))
                        
                        start_response('204 No Content', [])
                elif method == 'OPTIONS':
                    start_response('204 No Content', [('Allow', 'GET, OPTIONS, PATCH')])
                else:
                    start_response('405 Method Not Allowed', [('Allow', 'GET, OPTIONS, PATCH')])
            
            return item


class HtmlEndpoint(DBEndpoint[DeclarativeMeta_T]):
    def __init__(self, table: Type[DeclarativeMeta_T], session_maker: sessionmaker):
        super().__init__(table, session_maker)
        
        @self.endpoint('')
        def items(environ: wsgi.Environ, start_response: wsgi.StartResponse) -> wsgi.Iterable:
            response_headers = Headers()
            method = environ['REQUEST_METHOD']
            session: Session = session_maker()
            
            if method == 'GET':
                start_response('200 OK', response_headers.items())
                yield from buffered_join(map(attrgetter('id'), session.query(table).all()), '\n')
            else:
                start_response('405 Method Not Allowed', response_headers.items())
    
    def __getitem__(self, index: str) -> wsgi.Callable:
        try:
            return super().__getitem__(index)
        except ValueError:
            def item(environ: wsgi.Environ, start_response: wsgi.StartResponse) -> wsgi.Iterable:
                pass
            
            return item


def create_endpoint_func(endpoint_cls: Type[BranchEndpoint])\
        -> Callable[[sessionmaker], Callable[[Type], RestEndpoint[T]]]:
    
    def endpoint(*args, **kwargs) -> Callable[[Type], endpoint_cls[T]]:
        def decorator(cls: Type[T]) -> endpoint_cls[T]:
            return RestEndpoint(cls, *args, **kwargs)
        
        return decorator
    
    return endpoint


rest_endpoint = create_endpoint_func(RestEndpoint)
html_endpoint = create_endpoint_func(HtmlEndpoint)


def combined_endpoint(name: str, branches: Iterable[BranchEndpoint]) -> Callable[[Column_T], Column_T]:
    def decorator(f: Column_T) -> Column_T:
        for branch in branches:
            branch.endpoint(name)(f)
        
        return f
    
    return decorator
