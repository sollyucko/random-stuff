from enum import Enum, auto

from .common import JSSyntaxError


class Associativity(Enum):
	LEFT = auto()
	RIGHT = auto()


operator_priorities = [
	({'**'}, Associativity.RIGHT),
	({'*', '/'}, Associativity.LEFT),
	({'+', '-'}, Associativity.LEFT)
]


class OperatorCall:
	def __init__(self, char, *args):
		self.char = char
		self.args = args
	
	def __str__(self):
		if len(self.args) == 1:
			return '(' + self.char + str(self.args[0]) + ')'
		elif len(self.args) == 2:
			return '(' + str(self.args[0]) + self.char + str(self.args[1]) + ')'
	
	def __repr__(self):
		return f'{type(self).__name__}({self.char!r}, {", ".join(map(repr, self.args))})'


def generate_ast(paren_tree):
	paren_tree = [generate_ast(node) if isinstance(node, list) else node for node in paren_tree]
	
	for operators, associativity in operator_priorities:
		new = []
		
		if associativity == Associativity.LEFT:
			paren_tree_iterator = iter(paren_tree)
			
			for node in paren_tree_iterator:
				if str(node) in operators:
					if node.arg_count == 1:
						new.append(OperatorCall(node.src, next(paren_tree_iterator)))
					elif node.arg_count == 2:
						new.append(OperatorCall(node.src, new.pop(), next(paren_tree_iterator)))
				else:
					new.append(node)
			
			paren_tree = new
		
		elif associativity == Associativity.RIGHT:
			paren_tree_iterator = iter(reversed(paren_tree))
			
			for node in paren_tree_iterator:
				if str(node) in operators:
					if node.arg_count == 1:
						new.append(OperatorCall(node.src, new.pop()))
					elif node.arg_count == 2:
						new.append(OperatorCall(node.src, next(paren_tree_iterator), new.pop()))
				else:
					new.append(node)
			
			paren_tree = list(reversed(new))
	
	if len(paren_tree) == 1:
		return paren_tree[0]
	else:
		print(paren_tree)
		raise JSSyntaxError('Multiple expressions encountered without an operator in between')
