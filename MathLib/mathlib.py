#! /bin/python3 -i


import atexit

from collections import Counter
from math import sqrt
from itertools import chain, count
from pickle import dump, load
from sortedcontainers import SortedSet
from typing import Iterable

try:
	with open('cache.pickle', 'rb') as f:
		cache = load(f)
except FileNotFoundError:
	cache = dict()

if 'primes' not in cache:
	cache['primes'] = SortedSet()  # Type: Set[int]

if 'prime_factors' not in cache:
	cache['prime_factors'] = dict()  # Type: Dict[int, Counter]


def is_multiple(a, b):
	return a % b == 0


class _Primes:
	def __iter__(self) -> Iterable[int]:
		if cache['primes']:
			yield from cache['primes']
			current_primes = cache['primes']
			start = max(current_primes) + 1
		else:
			current_primes = SortedSet()
			start = 2
		
		for i in count(start):
			for p in current_primes:
				if is_multiple(i, p):
					break
			else:
				cache['primes'].add(i)
				current_primes.add(i)
				yield i
				
				if is_multiple(len(cache['primes']), 1000):
					save_cache()
	
	def __contains__(self, other) -> bool:
		if not isinstance(other, int):
			return False
		
		for prime in chain(cache['primes'], self):
			if prime == other or prime > sqrt(other):
				return True
			elif is_multiple(other, prime):
				return False


primes = _Primes()


def prime_factor(n: int) -> Iterable[int]:
	factors = Counter()
	
	prime_iterator = iter(primes)
	i = 0
	
	while i <= sqrt(n) and n > 1:
		i = next(prime_iterator)
		
		while is_multiple(n, i):
			yield i
			n //= i
			factors[i] += 1
	
	if n > 1:
		yield n
		factors[n] += 1
		cache['primes'].add(n)
	
	cache['prime_factors'][n] = factors


@atexit.register
def save_cache(*_):
	with open('cache.pickle', 'wb') as f:
		dump(cache, f)
