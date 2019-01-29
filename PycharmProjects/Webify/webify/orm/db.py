from pprint import pprint
from typing import (Any, Dict, Iterable, MutableMapping, Type,
                    Union, get_type_hints)

from sqlalchemy import Column, MetaData, Table, create_engine
# noinspection PyProtectedMember
from sqlalchemy.engine import Engine
from sqlalchemy.sql import sqltypes
from sqlalchemy.types import TypeEngine

SQLALCHEMY_TYPE_MAPPING: MutableMapping[Type, TypeEngine] = {}

for type_engine in vars(sqltypes).values():
    # noinspection PyBroadException
    try:
        python_type = type_engine().python_type
    except Exception:  # Can't do this with dict comprehensions.
        pass
    else:
        # Should select the least derived class due to the fact that they
        # should be defined first.
        SQLALCHEMY_TYPE_MAPPING.setdefault(python_type, type_engine)

pprint(SQLALCHEMY_TYPE_MAPPING)


def type_to_sqlalchemy(python_type: Type) -> TypeEngine:
    try:
        return SQLALCHEMY_TYPE_MAPPING[python_type]
    except KeyError:
        origin = python_type

        try:
            while True:
                origin = origin.__origin__
        except TypeError:
            raise  # For now

        # noinspection PyUnreachableCode
        if issubclass(origin, Iterable):
            pass  # TODO: create relationship? (using python_type.__args__)
        elif origin == Union:
            pass  # TODO: use enum?
        else:
            pass  # TODO: create table?


class DB:
    def __init__(self, engine: Union[str, Engine], **kwargs):
        if isinstance(engine, Engine):
            self.engine = engine
        else:
            self.engine = create_engine(engine, **kwargs)

        self.metadata = MetaData()

    def create_all(self):
        self.metadata.create_all(self.engine)

    def drop_all(self):
        self.metadata.drop_all(self.engine)


class TableRow:
    db: DB  # Class attribute
    table: Table  # Class attribute
    values: Dict[str, Any]  # Instance attribute

    def __init__(self, **values):
        self.values = values

    def register(self):
        self.db.engine.execute(self.table.insert(), **self.values)

    def __init_subclass__(cls, db: DB, table_name: str = None, **kwargs):
        if table_name is None:
            table_name = cls.__name__

        columns = (Column(name, type_to_sqlalchemy(python_type))
                   for name, python_type
                   in get_type_hints(cls).items())
        cls.table = Table(table_name, db.metadata, *columns)
        cls.db = db
