import sys
from itertools import cycle, tee


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


def mix(buckets, mix_count):  # type: (Iterable[Tuple[int, int]], int) -> Iterable[Tuple[int, int]]
    buckets_a, buckets_b = tee(map(list, buckets))
    
    for _, (a, b) in zip(range(mix_count), pairwise(cycle(buckets_a))):
        if a[1] + b[1] <= b[0]:
            b[1] += a[1]
            a[1] = 0
        else:
            a[1] -= b[0] - b[1]
            b[1] = b[0]
    
    return buckets_b


def main():
    print(*(x[1] for x in mix((map(int, input().split()) for _ in range(3)), 100)), sep='\n')


if __name__ == '__main__':
    with open('mixmilk.in') as file_in:
        with redirect_stdin(file_in):
            with open('mixmilk.out', 'w') as file_out:
                with redirect_stdout(file_out):
                    main()
