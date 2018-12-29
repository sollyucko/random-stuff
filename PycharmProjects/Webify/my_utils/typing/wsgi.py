from typing import (Any as _Any, Callable as _Callable, Dict as _Dict, Iterable as _Iterable, List as _List,
                    Tuple as _Tuple, Union as _Union)

from my_utils.typing import sys as _sys

EnvironKey = Status = ResponseHeaderKey = ResponseHeaderValue = str
EnvironValue = _Any
Environ = _Dict[EnvironKey, EnvironValue]
ResponseHeader = _Tuple[ResponseHeaderKey, ResponseHeaderValue]
ResponseHeaders = _List[ResponseHeader]

# (str) -> Any
Write = _Callable[[str], _Any]

# (wsgi.Status, wsgi.ResponseHeaders[, sys.ExcInfo]) -> wsgi.Write:
StartResponse = _Union[_Callable[[Status, ResponseHeaders], Write],
                       _Callable[[Status, ResponseHeaders, _sys.ExcInfo], Write]]

Iterable = _Iterable[str]

# (wsgi.Environ, wsgi.StartResponse) -> wsgi.Iterable:
Callable = _Callable[[Environ, StartResponse], Iterable]
