from __future__ import annotations

import hashlib
from typing import Any, Callable, Dict, Mapping, NoReturn, Optional, Tuple, Type, TypeVar, Union

from webify.db import DBValue, render_html_input, render_html_input_valued

__all__ = ['Email', 'Password']

T = TypeVar('T')


def create_hasher(name: str) -> Callable[[str], str]:
    def hasher(data: str, *args: Any, **kwargs: Any) -> str:
        return hashlib.new(name, data.encode('UTF-8')).hexdigest(*args, **kwargs)
    
    hasher.__name__ = name
    return hasher


class Password(DBValue):
    hashed: str
    hasher_name: str
    hashers: Dict[str, Callable[[str], str]] = {name: create_hasher(name) for name in hashlib.algorithms_available}
    
    def __init__(self, hashed: str, hasher_name: str) -> None:
        self.hashed = hashed
        self.hasher_name = hasher_name
    
    def __eq__(self, other: Any) -> Union[bool, Type[NotImplemented]]:
        if isinstance(other, Password):
            return self.hashed == other.hashed and self.hasher_name == other.hasher_name
        elif isinstance(other, str):
            return Password.from_value(other, self.hasher_name).hashed == self.hashed
        else:
            return NotImplemented
    
    @classmethod
    def from_value(cls: Type[Password], value: Union[str, Password], hasher_name: Optional[str] = None,
                   **kwargs: Any) -> Password:
        if isinstance(value, Password):
            return value
        elif isinstance(value, str):
            return cls(cls.hashers[hasher_name](value, **kwargs), hasher_name)
        else:
            raise TypeError(f'Can only convert str or Password to Password, not {type(value)}.')
    
    @classmethod
    def from_db(cls: Type[Password], value: str) -> Password:
        return cls(*value.split('$', 1))
    
    @classmethod
    def get_db_type(cls: Type[Password]) -> Tuple[Type[str], Dict[str, NoReturn]]:
        return str, {}
    
    def get_db_value(self: Password) -> str:
        return f'{self.hasher_name}${self.hashed}'
    
    @classmethod
    def to_html_input(cls: Type[Password]) -> str:
        return render_html_input('password')
    
    def to_html_input_valued(self: DBValue) -> str:
        return self.to_html_input()


class Email(DBValue):
    @classmethod
    def from_value(cls: Type[DBValue], value: Any, **kwargs: Any) -> DBValue:
        pass
    
    @classmethod
    def from_db(cls: Type[DBValue], value: Any) -> DBValue:
        pass
    
    @classmethod
    def get_db_type(cls: Type[DBValue]) -> Tuple[Type[T], Mapping[str, Any]]:
        pass
    
    def to_db_value(self: DBValue) -> T:
        pass
    
    @classmethod
    def to_html_input(cls: Type[DBValue]) -> str:
        return render_html_input('email')
    
    def to_html_input_valued(self: DBValue) -> str:
        return render_html_input_valued('email', str(self))
