import hashlib
from typing import Any, Callable, Dict, Optional, Tuple, Type, TypeVar, Union, NoReturn

from webify_v2.db import Column

__all__ = ['Password']

P = TypeVar('P', bound='Password')


def create_hasher(name: str) -> Callable[[str], str]:
    def hasher(data: str, *args: Any, **kwargs: Any) -> str:
        return hashlib.new(name, data.encode('UTF-8')).hexdigest(*args, **kwargs)
    
    hasher.__name__ = name
    return hasher


class Password(Column):
    hashed: str
    hasher_name: str
    hashers: Dict[str, Callable[[str], str]] = {name: create_hasher(name) for name in hashlib.algorithms_available}
    
    def __init__(self, hashed: str, hasher_name: str) -> None:
        self.hashed = hashed
        self.hasher_name = hasher_name
    
    def __eq__(self, other: Any) -> Union[bool, type(NotImplemented)]:
        if isinstance(other, Password):
            return self.hashed == other.hashed and self.hasher_name == other.hasher_name
        elif isinstance(other, str):
            return Password.from_value(other, self.hasher_name).hashed == self.hashed
        else:
            return NotImplemented
    
    @classmethod
    def from_value(cls: Type[P], value: Union[str, P], hasher_name: Optional[str] = None, **kwargs: Any) -> P:
        if isinstance(value, Password):
            return value
        elif isinstance(value, str):
            return cls(cls.hashers[hasher_name](value, **kwargs), hasher_name)
        else:
            raise TypeError(f'Can only convert str or Password to Password, not {type(value)}.')
    
    @classmethod
    def from_db(cls: Type[P], value: str) -> P:
        return cls(*value.split('$', 1))
    
    @classmethod
    def get_db_type(cls: Type[P]) -> Tuple[Type[str], Dict[str, NoReturn]]:
        return str, {}
    
    def get_db_value(self: P) -> str:
        return f'{self.hasher_name}${self.hashed}'
