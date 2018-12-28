import enum

from sly import Lexer, Parser

from syntax_utils import *


class Grouper(enum.Enum):
	PAREN = enum.auto()
	BRACKET = enum.auto()
	BRACE = enum.auto()
	
	@classmethod
	def from_char(cls, char: str) -> 'Grouper':
		if char in '()':
			return cls.PAREN
		elif char in '[]':
			return cls.BRACKET
		elif char in '{}':
			return cls.BRACE


# noinspection PyUnresolvedReferences,PyUnboundLocalVariable,PyPep8Naming,PyMethodMayBeStatic,PyRedeclaration
class CalcLexer(Lexer):
	tokens = {ID, NUMBER, GROUP_START, GROUP_END}
	ignore = ' \t'
	literals = set('=+-*/^,')
	
	ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
	NUMBER = a(r'\d+', int)
	
	def __init__(self):
		self.stack = []
	
	@_(r'\(|\[')
	def GROUP_START(self, t: Token):
		self.stack.append(Grouper.from_char(t.value))
		return t
	
	@_(r'\)|\]')
	def GROUP_END(self, t: Token):
		assert self.stack.pop() == Grouper.from_char(t.value)
		return t


# noinspection PyUnresolvedReferences,PyUnboundLocalVariable,PyPep8Naming,PyMethodMayBeStatic,PyRedeclaration,SpellCheckingInspection
class CalcParser(Parser):
	tokens = CalcLexer.tokens
	
	precedence = (
		('left', '+', '-'),
		('left', '*', '/'),
		('right', NEG)
	)
	
	# Rules where precedence is applied
	@_('expr "+" expr')
	def expr(self, p):
		return '+', [p.expr0, p.expr1]
	
	@_('expr "-" expr')
	def expr(self, p):
		return '-', [p.expr0, p.expr1]
	
	@_('expr "*" expr')
	def expr(self, p):
		return '*', [p.expr0, p.expr1]
	
	@_('expr "/" expr')
	def expr(self, p):
		return '/', [p.expr0, p.expr1]
	
	@_('"-" expr %prec NEG')
	def expr(self, p):
		return '-', [p.expr]
	
	@_('NUMBER')
	def expr(self, p):
		return p.NUMBER
	
	@_('GROUP_START expr GROUP_END')
	def expr(self, p):
		return p.expr


if __name__ == '__main__':
	lexer = CalcLexer()
	parser = CalcParser()
	
	while True:
		try:
			text = input('> ')
			result = parser.parse(lexer.tokenize(text))
			print(result)
		except EOFError:
			break
