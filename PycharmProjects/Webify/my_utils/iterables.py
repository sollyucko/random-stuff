from __future__ import annotations

from typing import Iterable, Iterator, MutableSequence, Union, TypeVar, overload


T = TypeVar("T")


class Reiterable(Iterable[T]):
    cache: MutableSequence[T]
    iterator: Iterator[T]
    slice_: slice

    # Python, why, oh, why do you have to have lowercase builtin types?
    def __init__(self, iterable: Iterable[T], slice_: slice = slice(None)):
        self.iterator = iter(iterable)
        self.cache = []
        self.slice_ = slice_

    def __iter__(self) -> Reiterator[T]:
        return Reiterator(self)

    @overload
    def __getitem__(self, index: int) -> T:
        ...

    @overload
    def __getitem__(self, index: slice) -> Reiterable[T]:
        ...

    def __getitem__(self, index: Union[int, slice]) -> Union["Reiterable[T]", T]:
        if isinstance(index, slice):
            return Reiterable(self, index)
        else:
            try:
                return self.cache[index]
            except IndexError:
                for _, x in zip(range(index - len(self.cache)), self.iterator):
                    self.cache.append(x)

                return self.cache[-1]


class Reiterator(Iterator[T]):
    def __init__(self, reiterable: Reiterable[T]):
        self.reiterable = reiterable
        self.i = reiterable.slice_.start or 0

    def __next__(self) -> T:
        stop = self.reiterable.slice_.stop

        if stop is not None and self.i >= stop:
            raise StopIteration("Cannot iterate past stop.")

        while self.i >= len(self.reiterable.cache):
            self.reiterable.cache.append(next(self.reiterable.iterator))

        try:
            return self.reiterable.cache[self.i]
        finally:
            self.i += self.reiterable.slice_.step or 1
