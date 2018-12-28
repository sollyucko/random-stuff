from string import digits
from typing import List


class Parser:
	def __init__(self):
		self.state_processors = {}
		self.char_processors = {}
	
	def tokenize(self, string):
		state = 'NONE'
		tokens = []
		
		for char in string:
			if state == 'NONE':
				state = self.char_processors[char](tokens)
			else:
				state = self.state_processors[state](tokens, char)
		
		if state != 'NONE':
			self.state_processors[state](tokens, '')
		
		if state != 'NONE':
			raise SyntaxError
		
		return tokens


class Token:
	pass


class Integer(Token):
	def __init__(self, text):
		self.value = int(text)
	
	def __str__(self):
		return str(self.value)
	
	def __repr__(self):
		return f'{self.__class__.__name__}({self.value!r})'


class String(Token):
	def __init__(self, text):
		self.value = text
	
	def __str__(self):
		return self.value
	
	def __repr__(self):
		return f'{self.__class__.__name__}({self.value!r})'


def install_integer_plugin(parser: Parser, digits=digits):
	def digit_processor(digit: str):
		def f(tokens: List[Token]):
			nonlocal current_state
			current_state = digit
			return 'INTEGER'
		
		return f
	
	def integer_processor(tokens: List[Token], char: str):
		nonlocal current_state
		
		if char == '':
			tokens.append(Integer(current_state))
			return 'NONE'
		elif char in digits:
			current_state += char
			return 'INTEGER'
		else:
			tokens.append(Integer(current_state))
			return parser.char_processors[char](tokens)
	
	current_state = ''
	
	parser.state_processors['INTEGER'] = integer_processor
	
	for digit in digits:
		parser.char_processors[digit] = digit_processor(digit)


def install_string_plugin(parser: Parser, delimiters='\'"'):
	def start_processor(delimiter: str):
		def f(tokens: List[Token]):
			nonlocal current_delimiter, current_state
			current_delimiter = delimiter
			current_state = ''
			return 'STRING'
		
		return f
	
	def char_processor(tokens: List[Token], char: str):
		nonlocal current_delimiter, current_state
		
		if char == current_delimiter:
			tokens.append(String(current_state))
			return 'NONE'
		else:
			current_state += char
			return 'STRING'
	
	current_state = ''
	current_delimiter = ''
	
	parser.state_processors['STRING'] = char_processor
	
	for delimiter in delimiters:
		parser.char_processors[delimiter] = start_processor(delimiter)


if __name__ == "__main__":
	parser = Parser()
	install_integer_plugin(parser)
	install_string_plugin(parser)

	while True:
		code = input('> ')
		print()
		print(*map(repr, parser.tokenize(code)), sep='\n', end='\n\n')
