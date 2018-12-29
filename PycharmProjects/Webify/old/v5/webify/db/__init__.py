from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import Field, MISSING, _FIELDS, dataclass, fields
from typing import Any, Container, Iterable, List, Mapping, Optional, Tuple, Type, TypeVar, Union
from warnings import warn

from webify import Managed

T = TypeVar('T')

__all__ = ['DBValue', 'DBRow', 'render_html_input', 'render_html_input_valued']


class DBValue(ABC):
    @classmethod
    @abstractmethod
    def from_value(cls: Type[DBValue], value: Any, **kwargs: Any) -> DBValue:
        pass
    
    @classmethod
    @abstractmethod
    def from_db(cls: Type[DBValue], value: Any) -> DBValue:
        pass
    
    @classmethod
    @abstractmethod
    def get_db_type(cls: Type[DBValue], *args: Any, **kwargs: Any) -> Tuple[Type, Iterable[Any], Mapping[str, Any]]:
        pass
    
    @abstractmethod
    def get_db_value(self: DBValue) -> Any:
        pass
    
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


class DBRow(Managed):
    primary_key: str  # Only defined if multiple_primary_keys
    
    # Only defined if not multiple_primary_keys
    primary_keys: Iterable[str]
    multiple_primary_keys: bool
    __dataclass_fields__: Mapping[str, Field]
    
    def __init_subclass__(cls, multiple_primary_keys=False, **kwargs):
        super().__init_subclass__(**kwargs)
        
        print(dir(cls))
        
        # noinspection PyMethodFirstArgAssignment
        cls = dataclass(cls)
        
        primary_keys: List[str] = []
        
        for field in fields(cls):
            if field.metadata.get('primary_key'):
                if primary_keys and not multiple_primary_keys:
                    raise ValueError('Multiple primary keys specified. '
                                     'Set multiple_primary_keys to true to allow multiple primary keys.')
                
                primary_keys.append(field.name)
            
            setattr(cls, field.name, create_field_property(field))
        
        if not primary_keys:
            if multiple_primary_keys:
                warn('No primary key specified -> only one possible primary key set -> limit of 1 row.')
            else:
                primary_keys = fields(cls)[:1]
        
        if multiple_primary_keys:
            cls.primary_keys = primary_keys
        else:
            cls.primary_key = primary_keys[0]
        
        cls.multiple_primary_keys = multiple_primary_keys
    
    @classmethod
    def get_instances(cls: Type[DBRow[T]]) -> DBRow[T]:
        pass
    
    @classmethod
    def get_instance_by_id(cls: Type[DBRow[T]], identifier: T) -> DBRow[T]:
        if cls.multiple_primary_keys:
            pass
        else:
            pass
    
    @property
    def identifier(self: DBRow[T]) -> T:
        return (tuple(getattr(self, pk) for pk in self.primary_keys)
                if self.multiple_primary_keys
                else getattr(self, self.primary_key))
    
    @property
    def all_fields(self: DBRow[T]) -> Mapping[str, Any]:
        return {name: getattr(self, name) for name in getattr(self, _FIELDS)}
    
    @property
    def preview_fields(self: DBRow[T]) -> Mapping[str, Any]:
        return {
            name: getattr(self, name)
            for name, field in getattr(self, _FIELDS)
            if field.metadata.get('PREVIEW') or field.metadata.get('PRIMARY_KEY')
        }
    
    def register(self: Managed[T]) -> None:
        pass


def get_db_value(value: DBValue, builtin_types: Iterable[Type[T]]) -> T:
    builtin_types = tuple(builtin_types)
    
    while not isinstance(value, builtin_types):
        value = value.get_db_value()
    
    return value


def get_db_type(data_type: Union[Type[DBValue], Type[T]], builtin_types: Container[Type[T]], args: Iterable[Any] = (),
                kwargs: Optional[Mapping[str, Any]] = None) -> Tuple[Type[T], Iterable[Any], Mapping[str, Any]]:
    if kwargs is None:
        kwargs = {}
    
    while data_type not in builtin_types:
        data_type, args, kwargs = data_type.get_db_type(*args, **kwargs)
    
    return data_type, args, kwargs


def create_field_property(field: Field) -> property:
    value = field.default if field.default_factory is MISSING else field.default_factory()
    
    @property
    def x(self):
        return value
    
    @x.setter
    def x(self, new_value):
        nonlocal value
        value = field.type.from_value(new_value, **field.metadata)
    
    return x
