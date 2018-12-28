from functools import wraps
from itertools import islice, tee


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


def get_region(board, x1, y1):  # type: (Sequence[Sequence[int]], int, int) -> Set[Tuple[int, int]]
    old_bales = set()
    new_bales = [(x1, y1)]
    
    while new_bales:
        bale = new_bales.pop()
        
        if bale not in old_bales:
            old_bales.add(bale)
            old_bales |= {(x2, y2) for x2, y2 in
                          ((max(bale[0] - 1, 0),                       bale[1]),
                           (bale[0],                                   min(bale[1] + 1, len(board) - 1)),
                           (min(bale[0] + 1, len(board[bale[1]]) - 1), bale[1]),
                           (bale[0],                                   max(bale[1] - 1, 0)))
                          if board[y1][x1] == board[y2][x2]}
    
    return old_bales


def process_board(board, region_min_size):  # type: (MutableSequence[MutableSequence[int]], int) -> None
    while True:
        bales_to_destroy = set()
        
        for y, row in enumerate(board):
            for x, bale in enumerate(row):
                if board[y][x]:
                    region = get_region(board, x, y)
                    
                    if len(region) >= region_min_size:
                        bales_to_destroy |= region
        
        if not bales_to_destroy:
            return
        else:
            for bale in bales_to_destroy:
                board[bale[1]][bale[0]] = 0
            
            # print('----------')
            # print('\n'.join(''.join(map(str, row)).replace('0', ' ') for row in board))
            # print('----------')
            
            loop = True
            
            while loop:
                loop = False
                
                for y in range(len(board) - 2, -1, -1):
                    for x in range(len(board[y])):
                        if board[y][x] and not board[y + 1][x]:
                            # print(x, y)
                            board[y + 1][x] = board[y][x]
                            board[y][x] = 0
                            
                            loop = True
            
            # print('----------')
            # print('\n'.join(''.join(map(str, row)).replace('0', ' ') for row in board))
            # print('----------')


def main(in_file, out_file):
    n, k = map(int, in_file.readline().split())
    board = [list(map(int, in_file.readline().strip())) for _ in range(n)]

    # print('----------')
    # print('\n'.join(''.join(map(str, row)).replace('0', ' ') for row in board))
    # print('----------')

    process_board(board, k)

    # print('----------')
    # print('\n'.join(''.join(map(str, row)).replace('0', ' ') for row in board))
    # print('----------')

    out_file.write('\n'.join(''.join(map(str, row)) for row in board))


if __name__ == '__main__':
    with open('mooyomooyo.in') as in_file:
        with open('mooyomooyo.out', 'w') as out_file:
            main(in_file, out_file)
