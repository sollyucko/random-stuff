import atexit
from itertools import count
from pickle import UnpicklingError, dump, load
from typing import Counter

from myutils import CachedIterable


def load_cache(filename='cache.pickle'):
    try:
        with open(filename, 'rb') as f:
            c = load(f)
    except (EOFError, FileNotFoundError, UnpicklingError):
        c = {}
    
    c.setdefault('primes', [2])
    c.setdefault('prime_factors', {})
    
    return c


cache = load_cache()


@atexit.register
def save_cache(filename='cache.pickle'):
    print('Saving...')
    
    with open(filename, 'wb') as f:
        dump(cache, f)


def _primes():
    for i in count(2):
        for j in primes:
            if i % j == 0:
                break
            elif j ** 2 > i:
                yield i
                break


primes = CachedIterable(_primes(), cache['primes'])


def prime_factor(n: int) -> Counter[int]:
    # noinspection PyTypeHints
    c = Counter()
    
    for p in primes:
        if p ** 2 > n:
            break
        
        while n % p == 0:
            c[p] += 1
            n //= p
    
    if n > 1:
        c[n] += 1
    
    return c
