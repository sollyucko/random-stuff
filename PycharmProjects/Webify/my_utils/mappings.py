from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from functools import partial
from itertools import chain
from typing import (
    Any,
    Callable,
    Container,
    Dict,
    ItemsView,
    Iterable,
    Iterator,
    KeysView,
    Mapping,
    Tuple,
    TypeVar,
    Union,
    ValuesView,
)

from more_itertools import unique_everseen

from my_utils.functions import constant, wrap
from my_utils.iterables import Reiterable

K = TypeVar("K")
T = TypeVar("T")
V = TypeVar("V")


class IterableContainer(Container[T], Iterable[T]):
    def __init__(
        self, iterable: Iterable[T], pretest: Callable[[T], bool] = constant(True)
    ):
        self.iterable = iterable
        self.pretest = pretest

    def __iter__(self) -> Iterator[T]:
        return iter(self.iterable)

    def __contains__(self, item: Any) -> bool:
        if not self.pretest(item):
            return False

        for x in self.iterable:
            if x == item:
                return True

        return False


class ContainerUnion(Container[T]):
    def __init__(self, containers: Iterable[Container[T]]):
        self.containers = containers

    def __contains__(self, item: Any) -> bool:
        for container in self.containers:
            if item in container:
                return True

        return False


class RecursiveMapping(Mapping[K, Union[V, "RecursiveMapping[K, V]"]], ABC):
    pass


class RecursiveDefaultDict(Dict[K, Union[V, "RecursiveDefaultDict[K, V]"]]):
    def __missing__(self, key: K) -> RecursiveDefaultDict[K, V]:
        return RecursiveDefaultDict()


@dataclass(init=False)
class ChainMapOfIterables(Mapping[K, Iterable[V]]):
    mappings: Iterable[Mapping[K, Iterable[V]]]

    def __init__(self, *mappings: Mapping[K, Iterable[V]]):
        self.mappings = mappings

    @classmethod
    def from_iterable(cls, mappings: Iterable[Mapping[K, Iterable[V]]]):
        instance: ChainMapOfIterables = cls()
        instance.mappings = mappings
        return instance

    def __getitem__(self, key: K) -> Iterable[V]:
        return chain.from_iterable(mapping.get(key, ()) for mapping in self.mappings)

    def __iter__(self) -> Iterator[K]:
        return chain.from_iterable(self.mappings)

    def __len__(self):
        return len(tuple(self))


@dataclass(init=False)
class MapZip(Mapping[K, Tuple[V, ...]]):  # len(map_zip[...]) == len(map_zip.mappings)
    mappings: Tuple[Mapping[K, V], ...]

    def __init__(self, *mappings: Mapping[K, V]):
        self.mappings = mappings

    def __getitem__(
        self, key: K
    ) -> Tuple[V, ...]:  # len(map_zip[...]) == len(map_zip.mappings)
        return tuple(mapping[key] for mapping in self.mappings)

    @wrap(unique_everseen)
    def __iter__(self) -> Iterator[K]:
        if self.mappings:
            for key in self.mappings[0]:
                for mapping in self.mappings[1:]:
                    if key not in mapping:
                        break
                else:
                    yield key

    def __len__(self):
        return max(map(len, self.mappings))


@dataclass(init=False)
class MapZipWithDefault(MapZip):
    default: V

    def __init__(self, *mappings: Mapping[K, Iterable[V]], default: V = None):
        super().__init__(*mappings)
        self.default = default

    def __getitem__(
        self, key: K
    ) -> Tuple[V, ...]:  # len(map_zip[...]) == len(map_zip.mappings)
        return tuple(mapping.get(key, self.default) for mapping in self.mappings)

    @wrap(unique_everseen)
    def keys(self) -> Iterable[K]:
        # Probably faster than "bitwise" or-ing. (Not timed.)
        for mapping in self.mappings:
            yield from mapping.keys()
