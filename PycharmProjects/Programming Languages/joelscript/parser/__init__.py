from .ast import generate_ast
from .common import JSSyntaxError
from .paren_tree import generate_paren_tree
from .tokenizer import tokenize


def parse(code):
	return generate_ast(generate_paren_tree(tokenize(code)))


if __name__ == '__main__':
	while True:
		try:
			print(parse(input('> ')))
		except JSSyntaxError as e:
			print('Syntax error:', e)
