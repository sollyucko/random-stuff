from types import TracebackType
from typing import Callable, Dict, Iterable, List, Tuple, Type, Union, TypeVar

__all__ = ['Environ', 'Header', 'Headers', 'Output', 'StartResponse', 'Status', 'WSGIApp', 'Write']

# '''({str -> str}, (str, [(str, str)]) -> (str) -> None) -> Iterable[str]'''
Environ = Dict[str, str]
Status = str
Header = Tuple[str, str]
Headers = List[Header]
Write = Callable[[str], None]
Ex = TypeVar('Ex', BaseException)
ExcInfo = Tuple[Type[Ex], Ex, TracebackType]
StartResponse = Union[Callable[[Status, Headers], Write], Callable[[Status, Headers, ExcInfo], Write]]
Output = Iterable[str]
WSGIApp = Callable[[Environ, StartResponse], Output]
