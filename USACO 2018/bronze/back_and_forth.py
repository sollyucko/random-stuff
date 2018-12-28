import sys
from itertools import tee


# From docs (https://docs.python.org/3.4/library/itertools.html)


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


def pass_through(f, o):
    f(o)
    return o


def get_readings(barns, num_days):  # (Iterable[Tuple[int, Iterable[int]]], int) -> Iterable[int]
    possibilities = {tuple((tank, tuple(buckets)) for tank, buckets in barns)}
    
    for d in range(num_days):
        temp = possibilities
        possibilities = set()
        
        for possibility in temp:
            from_i = d % len(possibility)
            from_barn = possibility[from_i]
            to_i = (d + 1) % len(possibility)
            
            for bucket in from_barn[1]:
                new_buckets = list(from_barn[1])
                new_buckets.remove(bucket)
                
                possibilities.add(tuple(
                    ((tank - bucket, tuple(new_buckets)) if i == from_i
                     else ((tank + bucket, buckets + (bucket,)) if i == to_i
                           else (tank, buckets)))
                    for i, (tank, buckets) in enumerate(possibility)))
    
    return possibilities


def main():
    print(len(set(x[0][0] for x in get_readings(((1000, map(int, input().split())) for _ in range(2)), 4))))


if __name__ == '__main__':
    with open('backforth.in') as file_in:
        with redirect_stdin(file_in):
            with open('backforth.out', 'w') as file_out:
                with redirect_stdout(file_out):
                    main()
