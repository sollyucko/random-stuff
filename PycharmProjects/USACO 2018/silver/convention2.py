from functools import wraps
from itertools import chain, islice, product, tee


# From docs (https://docs.python.org/3.4/library/itertools.html#itertools-recipes)

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


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


def calculate_wait_times(cows):  # (Iterable[Tuple[int, int]]) -> Iterable[int]
    cows = tuple([start, length, True] for (start, length) in cows)
    
    if not cows:
        return
    
    yield 0
    current_cow = min(cows, key=lambda cow: cow[0])
    # print(current_cow, 0)
    current_time = current_cow[0] + current_cow[1]
    current_cow[2] = False
    
    for _ in range(len(cows) - 1):
        try:
            current_cow = list(cow for cow in cows if cow[2] and cow[0] <= current_time)[0]
        except IndexError:
            current_cow = min((cow for cow in cows if cow[2]), key=lambda cow: cow[0])
            current_time = current_cow[0]
        
        yield current_time - current_cow[0]
        # print(current_cow, current_time - current_cow[0])
        
        current_time += current_cow[1]
        current_cow[2] = False


def main(in_file, out_file):
    out_file.write(str(max(calculate_wait_times(map(int, in_file.readline().split()) for _ in range(int(in_file.readline()))))))


if __name__ == '__main__':
    for i in range(10000):
        with open('convention2.in') as in_file:
            with open('convention2.out', 'w') as out_file:
                main(in_file, out_file)
