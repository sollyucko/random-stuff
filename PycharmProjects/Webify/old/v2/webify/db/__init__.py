from abc import ABC, abstractmethod
from dataclasses import Field, MISSING, _FIELDS, dataclass, fields
from typing import Any, Container, Iterable, List, Mapping, Optional, Tuple, Type, TypeVar, Union
from warnings import warn

from webify_v2 import Managed
from .types import *
from .types import __all__ as _types_all

Column_T = TypeVar('Column_T', bound='Column')
T = TypeVar('T')
Table_T = TypeVar('Table_T', bound='Table')

__all__ = ['Column', 'Table'] + _types_all


class Column(ABC):
    @classmethod
    @abstractmethod
    def from_value(cls: Type[Column_T], value: Any, **kwargs: Any) -> Column_T:
        pass
    
    @classmethod
    @abstractmethod
    def from_db(cls: Type[Column_T], value: Any) -> Column_T:
        pass
    
    @classmethod
    @abstractmethod
    def get_db_type(cls: Type[Column_T], *args: Any, **kwargs: Any) -> Tuple[Type, Iterable[Any], Mapping[str, Any]]:
        pass
    
    @abstractmethod
    def get_db_value(self: Column_T) -> Any:
        pass


class Table(Managed):
    primary_key: str  # Only defined if multiple_primary_keys
    
    # Only defined if not multiple_primary_keys
    primary_keys: Iterable[str]
    multiple_primary_keys: bool
    __dataclass_fields__: Mapping[str, Field]
    
    def __init_subclass__(cls, multiple_primary_keys=False, **kwargs):
        super().__init_subclass__(**kwargs)
        
        primary_keys: List[str] = []
        
        for field in fields(dataclass(cls)):  # Makes cls into a dataclass in-place
            if field.metadata.get('PRIMARY_KEY'):
                if cls.primary_keys and not multiple_primary_keys:
                    raise ValueError('Multiple primary keys specified. '
                                     'Set multiple_primary_keys to true to allow multiple primary keys.')
                
                primary_keys.append(field.name)
            
            setattr(cls, field.name, create_field_property(field))
        
        if not primary_keys:
            if multiple_primary_keys:
                warn('No primary key specified -> only one possible primary key set -> limit of 1 row.')
            else:
                raise ValueError('No primary key specified.')
        
        if multiple_primary_keys:
            cls.primary_keys = primary_keys
        else:
            cls.primary_key = primary_keys[0]
        
        cls.multiple_primary_keys = multiple_primary_keys
    
    @classmethod
    def get_instances(cls: Type[Table_T[T]]) -> Table_T[T]:
        pass
    
    @classmethod
    def get_instance_by_id(cls: Type[Table_T[T]], identifier: T) -> Table_T[T]:
        if cls.multiple_primary_keys:
            pass
        else:
            pass
    
    @property
    def id(self: Table_T[T]) -> T:
        return (tuple(getattr(self, pk) for pk in self.primary_keys)
                if self.multiple_primary_keys
                else getattr(self, self.primary_key))
    
    @property
    def all_fields(self: Table_T[T]) -> Mapping[str, Any]:
        return {name: getattr(self, name) for name in getattr(self, _FIELDS)}
    
    @property
    def preview_fields(self: Table_T[T]) -> Mapping[str, Any]:
        return {
            name: getattr(self, name)
            for name, field in getattr(self, _FIELDS)
            if field.metadata.get('PREVIEW') or field.metadata.get('PRIMARY_KEY')
        }


def get_db_value(value: Column, builtin_types: Iterable[Type[T]]) -> T:
    builtin_types = tuple(builtin_types)
    
    while not isinstance(value, builtin_types):
        value = value.get_db_value()
    
    return value


def get_db_type(data_type: Union[Type[Column], Type[T]], builtin_types: Container[Type[T]], args: Iterable[Any] = (),
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
