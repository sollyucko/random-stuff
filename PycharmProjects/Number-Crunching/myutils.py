from itertools import islice
from math import ceil
from signal import SIGTERM, signal
from sys import byteorder, exit
from typing import Callable, Generic, Iterable, Iterator, List, Optional, TypeVar, Union

__all__ = ['CachedIterable', 'integer_to_bytes', 'bytes_to_integer', 'integers_to_bytes', 'bytes_to_integers',
           'read_file', 'read_file_binary', 'overwrite_file', 'overwrite_file_binary',
           'run']

T = TypeVar('T')


class CachedIterable(Generic[T], Iterable[T]):
    cache: List[T]
    iterator: Iterator[T]
    
    def __init__(self, iterable: Iterable[T], cache: Optional[List[T]] = None):
        self.iterator = iter(iterable)
        self.cache = [] if cache is None else cache
    
    def __iter__(self) -> '_CachedIterator[T]':
        return _CachedIterator(self)
    
    def __getitem__(self, i: Union[slice, int]) -> T:
        try:
            # noinspection PyStatementEffect
            self[max(i.start, i.stop)]
            return self.cache[i]
        except AttributeError:
            try:
                return self.cache[i]
            except IndexError:
                return next(islice(self, i, None))


class _CachedIterator(Iterator[T], Generic[T]):
    i: int
    cached_iterable: CachedIterable[T]
    
    def __init__(self, it: CachedIterable[T]):
        self.cached_iterable = it
        self.i = 0
    
    def __next__(self) -> T:
        if self.i < len(self.cached_iterable.cache):
            result = self.cached_iterable.cache[self.i]
        else:
            val = next(self.cached_iterable.iterator)
            self.cached_iterable.cache.append(val)
            result = val
        
        self.i += 1
        
        return result


signal(SIGTERM, lambda *args: exit())


def integer_to_bytes(x: int) -> bytes:
    return x.to_bytes(ceil(x.bit_length() / 8), byteorder)


def bytes_to_integer(b: bytes) -> int:
    return int.from_bytes(b, byteorder)


def bytes_to_integers(b: bytes) -> List[int]:
    result = []
    i = 0
    
    while i < len(b):
        l = b[i]
        result.append(bytes_to_integer(b[i: i + l]))
        i += l
    
    return result


def integers_to_bytes(l: List[int]) -> bytes:
    return b''.join(map(integer_to_bytes, l))


def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def read_file_binary(filename: str) -> bytes:
    with open(filename, 'rb') as f:
        return f.read()


def overwrite_file(filename: str, data: str) -> None:
    with open(filename, 'w') as f:
        f.write(data)


def overwrite_file_binary(filename: str, data: bytes) -> None:
    with open(filename, 'wb') as f:
        f.write(data)


def run(f: Callable[[], T]) -> Callable[[], T]:
    f()
    return f
