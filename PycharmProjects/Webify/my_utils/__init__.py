from abc import ABC
from typing import Dict, TypeVar, Union, Generic, Mapping, Any

K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')


class RecursiveMapping(Generic[K, V], Mapping[K, Union[V, 'RecursiveMapping[K, V]']], ABC):
    pass


class RecursiveDefaultDict(RecursiveMapping[K, V], Dict[K, Union[V, 'RecursiveDefaultDict[K, V]']]):
    def __getitem__(self, key: K) -> Union['RecursiveDefaultDict[K, V]', V]:
        return self.setdefault(key, RecursiveDefaultDict())


class ChainMapOfIterables(Generic[K, V], Mapping[K, Iterable[V]]):
    mappings: Iterable[Mapping[K, Iterable[V]]]
    overrides: Dict[Any, Any]

    def __init__(self, mappings: Iterable[Mapping[K, Iterable[V]]]):
        self.mappings = mappings
        self.overrides = {}

    def __getitem__(self, key: K) -> Iterable[V]:
        try:
            return self.overrides[key]
        except KeyError:
            return chain.from_iterable(mapping.get(key, ()) for mapping in self.mappings)

    def __setitem__(self, key: K, value: Iterable[V]):
        self.overrides[key] = value

    def __delitem__(self, key):
        del self.overrides[key]

        for mapping in self.mappings:
            del mapping[key]
