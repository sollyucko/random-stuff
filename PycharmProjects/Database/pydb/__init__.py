from abc import ABC, abstractmethod
from collections import deque
from operator import itemgetter

from typing import Dict, List, Tuple, Type, TypeVar

from new_stdlib.io import Readable, Writable

DO = TypeVar('DO', bound='BaseDataObject')
DB = TypeVar('DB', bound='Database')

Properties = List[Tuple[str, Type['DataObject']]]
PropertiesRegistry = Dict[Type['DataObject'], Properties]


class Database:
    root_object: 'BaseDataObject'
    
    @classmethod
    def load(cls: Type[DB], input_stream: Readable[bytes]) -> DB:
        db = cls()
        preload_queue = deque((cls.load_start_type(input_stream)))
        load_queue = deque()
        objects = []
        
        while preload_queue:
            next_type = preload_queue.popleft()
            load_queue.append(next_type)
            preload_queue.extend(next_type.preload(db, input_stream))

        while load_queue:
            objects.append(load_queue.popleft().load(db, input_stream))
            
        db.root_object = objects[0]

        return db
    
    def store(self, output_stream: Writable[bytes]) -> None:
        pass
    
    @classmethod
    def load_metadata(cls, input_stream: Readable[bytes]) -> PropertiesRegistry:
        pass


class BaseDataObject(ABC):
    @classmethod
    @abstractmethod
    def preload(cls, database: Database, input_stream: Readable[bytes]) -> List[Type['BaseDataObject']]:
        pass
    
    @classmethod
    @abstractmethod
    def load(cls: Type[DO], database: Database, input_stream: Readable[bytes]) -> DO:
        pass


class DataObject:
    properties: Properties
    
    def __init_subclass__(cls, **kwargs):
        cls.properties = []
        
        for name, annotation in cls.__annotations__.items():
            if isinstance(annotation, type) and issubclass(annotation, DataObject):
                cls.properties.append((name, annotation))
        
        cls.properties.sort()
    
    @classmethod
    def preload(cls, database: Database, _: Readable[bytes]) -> List[Type[BaseDataObject]]:
        return list(map(itemgetter(1), cls.properties))
    
    @classmethod
    def load(cls: Type[DO], database: Database, input_stream: Readable[bytes]) -> DO:
        obj = cls()
        
        for name, data_type in cls.properties:
            setattr(obj, name, data_type.load(database, input_stream))
        
        return obj