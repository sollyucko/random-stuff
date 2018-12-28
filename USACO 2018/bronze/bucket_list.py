import sys


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


def count_buckets(cows, start_time, end_time):  # Type: (Iterable[Tuple[int, int, int]], int, int) -> Iterable[int]
    cows = tuple(cows)
    
    for t in range(start_time, end_time):
        yield sum(bucket_count for start, end, bucket_count in cows if start <= t <= end)


def main():
    print(max(count_buckets((tuple(map(int, input().split())) for _ in range(int(input()))), 1, 1000)))


if __name__ == '__main__':
    with open('blist.in') as file_in:
        with redirect_stdin(file_in):
            with open('blist.out', 'w') as file_out:
                with redirect_stdout(file_out):
                    main()
