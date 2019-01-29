from types import TracebackType as _TracebackType
from typing import Tuple as _Tuple, Type as _Type, TypeVar as _TypeVar

_E = _TypeVar('_E', bound=BaseException)

ExcInfo = _Tuple[_Type[_E], _E, _TracebackType]
