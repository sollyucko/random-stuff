from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Mapping, Tuple, Type, TypeVar, Optional

T = TypeVar('T')


class DBValue(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    def from_value(cls: Type[DBValue], value: Any, **kwargs: Any) -> DBValue:
        ...
    
    @classmethod
    @abstractmethod
    def from_db(cls: Type[DBValue], value: Any) -> DBValue:
        ...
    
    @classmethod
    @abstractmethod
    def get_db_type(cls: Type[DBValue]) -> Tuple[Type[T], Mapping[str, Any]]:
        ...
    
    @abstractmethod
    def to_db_value(self: DBValue) -> T:
        ...

    @classmethod
    @abstractmethod
    def to_html_input(cls: Type[DBValue]) -> str:
        ...

    @abstractmethod
    def to_html_input_valued(self: DBValue) -> str:
        ...


def render_html_input(input_type: str) -> str:
    return f'<input type="{input_type}" />'


def render_html_input_valued(input_type: str, value: str) -> str:
    return f'<input type="{input_type}" value="{value}" />'
