try:
	from .parser import parse
	from .parser.ast import OperatorCall
	from .parser.common import Float, Integer, JSSyntaxError, String
	from .new_runtime_2 import Runtime
except ImportError:
	from parser import parse
	from parser.ast import OperatorCall
	from parser.common import Float, Integer, JSSyntaxError, String
	from new_runtime_2 import Runtime


class Interpreter:
	def __init__(self):
		self.runtime = Runtime()
	
	def interpret(self, ast):
		if isinstance(ast, Float):
			return self.runtime.from_native(float(str(ast)))
		if isinstance(ast, Integer):
			return self.runtime.from_native(int(str(ast)))
		if isinstance(ast, String):
			return self.runtime.from_native(str(ast))
		elif isinstance(ast, OperatorCall):
			return self.runtime.operator(ast.char, list(map(self.interpret, ast.args)))


def interpret(ast):
	return Interpreter().interpret(ast)


# solly, make it also run from files
# later, basics/essentials first

def run_repl():
	while True:
		try:
			print(interpret(parse(input('> '))))
		except JSSyntaxError as e:
			print('Syntax error:', e)
