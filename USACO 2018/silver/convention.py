import gc
import sys
from functools import wraps
from itertools import chain, islice, product, tee


# From docs (https://docs.python.org/3.4/library/itertools.html#itertools-recipes)


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


# From Python 3.7's contextlib.py

class _RedirectStream:
    _stream = None
    
    def __init__(self, new_target):
        self._new_target = new_target
        # We use a list of old targets to make this CM re-entrant
        self._old_targets = []
    
    def __enter__(self):
        self._old_targets.append(getattr(sys, self._stream))
        setattr(sys, self._stream, self._new_target)
        return self._new_target
    
    def __exit__(self, exctype, excinst, exctb):
        setattr(sys, self._stream, self._old_targets.pop())


class redirect_stdout(_RedirectStream):
    _stream = "stdout"


# My code

class redirect_stdin(_RedirectStream):
    _stream = "stdin"


def chunked(iterable, n):  # (Iterable[T], int) -> Iterable[Tuple[T, ...]]
    iterator = iter(iterable)
    chunk = tuple(islice(iterator, n))
    
    while chunk:
        yield chunk
        chunk = tuple(islice(iterator, n))


def chunked_variable(iterable, sizes):  # (Iterable[T], Iterable[int]) -> Iterable[Tuple[T, ...]]
    iterator = iter(iterable)
    size_iterator = iter(sizes)
    chunk = tuple(islice(iterator, next(size_iterator)))
    
    while chunk:
        yield chunk
        chunk = tuple(islice(iterator, next(size_iterator)))


def cached_iterable(f):
    cache = {}
    
    @wraps(f)
    def decorated(*args):
        try:
            result = cache[args]
        except KeyError:
            result = f(*args)
        
        cache[args], result = tee(result)
        return result
    
    return decorated


def compose(*compose_args):
    def composition(x):
        for f in reversed(compose_args):
            x = f(x)
        
        return x
    
    return composition


def curried_compose(wrapper, *outer_args, **outer_kwargs):
    def decorator(f):
        def decorated(*inner_args, **inner_kwargs):
            return wrapper(f(*inner_args, **inner_kwargs), *outer_args, **outer_kwargs)
        
        return decorated
    
    return decorator


@cached_iterable
@curried_compose(set)
def possible_chunk_sizes(n, max_value=None, max_length=None):  # (int) -> Iterable[Iterable[int]]
    if n:
        if (max_value is None or n <= max_value) and (max_length is None or 1 <= max_length):
            yield (n,)
        
        for i in range(1, n):
            for x in product(possible_chunk_sizes(i, max_value, max_length), possible_chunk_sizes(n - i, max_value, max_length)):
                chunk = tuple(chain(*x))
                
                if max_length is None or len(chunk) <= max_length:
                    yield chunk


def wait_times(cows, seats):  # (Iterable[int], int) -> Iterable[int]
    for bus in chunked_variable(cows, seats):
        yield bus[-1] - bus[0]


def main():
    num_cows, num_buses, max_seats = map(int, input().split())
    cows = list(map(int, input().split()))
    cows.sort()
    print(max(chain.from_iterable(wait_times(cows, seats) for seats in possible_chunk_sizes(num_cows, max_seats, num_buses))))


if __name__ == '__main__':
    with open('convention.in') as file_in:
        with redirect_stdin(file_in):
            with open('convention.out', 'w') as file_out:
                with redirect_stdout(file_out):
                    main()
