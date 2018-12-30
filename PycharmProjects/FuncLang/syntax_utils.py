from functools import wraps
from typing import Callable, Any
# noinspection PyProtectedMember
from sly.lex import LexerMeta, Token


def value_processor(f):
	# noinspection PyUnusedLocal
	@wraps(f)
	def g(self, t: Token):
		t.value = f(t.value)
		return t
	
	return g


def a(regex: str, processor: Callable[[str], Any]):
	return LexerMeta.__prepare__(None, None)['_'](regex)(value_processor(processor))


