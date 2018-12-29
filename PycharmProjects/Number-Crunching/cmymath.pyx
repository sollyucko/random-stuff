# cython: language_level=3
import atexit
from itertools import count
from typing import Counter

from myutils import (CachedIterable, bytes_to_integers, read_file_binary, integers_to_bytes,
                     overwrite_file_binary, run)

cdef list prime_cache

@run
def load_cache():
    global prime_cache
    
    try:
        prime_cache = bytes_to_integers(read_file_binary('primes'))
    except FileNotFoundError:
        prime_cache = [2]

@atexit.register
def save_cache():
    overwrite_file_binary('primes', integers_to_bytes(prime_cache))

def _primes():
    cdef int j
    
    for i in count(2):
        for j in primes:
            if i % j == 0:
                break
            elif j ** 2 > i:
                yield i
                break

primes = CachedIterable(_primes(), prime_cache)

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
