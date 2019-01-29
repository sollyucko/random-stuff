from functools import reduce
from itertools import count, product, starmap
from operator import and_
# from typing import Callable, Iterable, Iterator, TypeVar, overload, Any

# T = TypeVar('T')
# U = TypeVar('U')
# V = TypeVar('V')
# W = TypeVar('W')
# X = TypeVar('X')


class Reiterable:#(Iterable[T]):
    # I blame Python for having lowercase builtin types :)
    def __init__(self, iterable: 'Iterable[T]', slice: 'slice' = slice(None)):
        self.iterator = iter(iterable)
        self.cache = []
        self.slice = slice
    
    def __iter__(self) -> 'Reiterator[T]':
        return Reiterator(self)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return Reiterable(self, index)
        else:
            try:
                return self.cache[index]
            except IndexError:
                for _, x in zip(range(index - len(self.cache)), self.iterator):
                    self.cache.append(x)
                
                return self.cache[-1]


class Reiterator:#(Iterator[T]):
    def __init__(self, reiterable: 'Reiterable[T]'):
        self.reiterable = reiterable
        self.i = reiterable.slice.start or 0
    
    def __next__(self):
        stop = self.reiterable.slice.stop
        
        if stop is not None and self.i >= stop:
            raise StopIteration('Cannot iterate past stop.')
        
        while self.i >= len(self.reiterable.cache):
            self.reiterable.cache.append(next(self.reiterable.iterator))
        
        try:
            return self.reiterable.cache[self.i]
        finally:
            self.i += self.reiterable.slice.step or 1


def overlap(first_iterable: 'Iterable[T]' = (), *iterables: 'Iterable[T]') -> 'Iterable[T]':
    reiterables = tuple(map(Reiterable, iterables))
    positions = [0] * len(iterables)
    
    for x in first_iterable:
        for i, reiterable, position in zip(count(), reiterables, positions):
            for j, y in enumerate(reiterable[position:]):
                if x == y:
                    positions[i] += j
                    break
            else:
                break
        else:
            yield x


# @formatter:off
# @overload
# def compose() -> Callable[[T], T]: ...
# @overload
# def compose(f1: Callable[[T], U]) -> Callable[[T], U]: ...
# @overload
# def compose(f1: Callable[[T], U], f2: Callable[[U], V]) -> Callable[[T], V]: ...
# @overload
# def compose(f1: Callable[[T], U], f2: Callable[[U], V], f3: Callable[[V], W]) -> Callable[[T], W]: ...
# @overload
# def compose(f1: Callable[[T], U], f2: Callable[[U], V], f3: Callable[[V], W], *fs: Callable[[Any], X]) -> Callable[[T], X]: ...
# @overload
# def compose(*fs: Callable[[T], T]) -> Callable[[T], T]: ...
# @formatter:on
def compose(*transformations: 'Callable') -> 'Callable':
    def f(x):
        for transformation in transformations:
            x = transformation(x)
        
        return x
    
    return f


def main():
    with open('int-test-input.txt') as in_f:
        for line in in_f:
            split = line.split()
            results = (set(overlap(*f(split))) for f in starmap(compose, product((compose(), reversed), (compose(), lambda x: tuple(map(reversed, x))))))
            combined_result = sorted(reduce(and_, results))
            print(''.join(combined_result))


if __name__ == '__main__':
    main()
