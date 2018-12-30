from enum import Enum, auto
from string import digits, whitespace

from bidict import bidict

from .common import EndParen, Integer, JSSyntaxError, Operator, StartParen, String

operators = {
	'+': {1, 2},
	'-': {1, 2},
	'*': {2},
	'/': {2},
	'**': {2}
}

parens = bidict({
	'(': ')',
	'[': ']',
	'{': '}'
})


class State(Enum):
	NONE = auto()
	INT = auto()
	FLOAT = auto()
	STR = auto()
	STR_ESC = auto()
	OPERATOR = auto()


def get_state_by_start_char(char, previous, result_new=[]):
	previous = result_new[-1] if result_new else previous
	if char in whitespace:
		return State.NONE, '', result_new
	elif char in digits:
		return State.INT, char, result_new
	elif char == '.':
		return State.FLOAT, char, result_new
	elif char in '\'\"':
		return State.STR, ('', char), result_new
	elif char in operators:
		if len([operator for operator in operators.keys() if operator.startswith(char)]) == 1:
			if len(operators[char]) == 1:
				return State.NONE, '', result_new + [Operator(char, next(iter(operators[char])))]
			elif operators[char] == {1, 2}:
				if previous == None or isinstance(previous, Operator):
					return State.NONE, '', result_new + [Operator(char, 1)]
				else:
					return State.NONE, '', result_new + [Operator(char, 2)]
		else:
			return State.OPERATOR, char, result_new
	elif char in parens.keys():
		return State.NONE, '', result_new + [StartParen(char)]
	elif char in parens.values():
		return State.NONE, '', result_new + [EndParen(char)]
	else:
		raise JSSyntaxError(f"Unexpected '{char}'", ('<string>', 0, 0, char))


def process_state(state_type, state, char, previous):
	if state_type == State.NONE:
		return get_state_by_start_char(char, previous)
	
	elif state_type == State.INT:
		if char == '':
			return State.NONE, '', [Integer(state)]
		elif char in digits:
			return State.INT, state + char, []
		elif char == '.':
			return State.FLOAT, state + char, []
		else:
			return get_state_by_start_char(char, previous, [Integer(state)])
	
	elif state_type == State.FLOAT:
		if char == '':
			return State.NONE, '', [Integer(state)]
		elif char in digits:
			return State.FLOAT, state + char, []
		else:
			return get_state_by_start_char(char, previous, [Integer(state)])
	
	elif state_type == State.STR:
		if char == '':
			raise JSSyntaxError('Unexpected EOL', ('<string>', 0, 0, '[EOL]'))
		elif char == state[1]:
			return State.NONE, '', [String(repr(state[0]))]
		elif char == '\\':
			return State.STR_ESC, state, []
		else:
			return State.STR, (state[0] + char, state[1]), []
	
	elif state_type == State.STR_ESC:
		if char == 'n':
			return State.STR, (state[0] + '\n', state[1]), []
		elif char == 't':
			return State.STR, (state[0] + '\t', state[1]), []
		elif char == '\\':
			return State.STR, (state[0] + '\\', state[1]), []
		else:
			return State.STR, (state[0] + char, state[1]), []
	
	elif state_type == State.OPERATOR:
		num_possibilities = len([operator for operator in operators.keys() if operator.startswith(state + char)])
		if num_possibilities == 1:
			if len(operators[state + char]) == 1:
				return State.NONE, '', [Operator(state + char, next(iter(operators[state + char])))]
			elif operators[state + char] == {1, 2}:
				if previous == None or isinstance(previous, Operator):
					return State.NONE, '', [Operator(state + char, 1)]
				else:
					return State.NONE, '', [Operator(state + char, 2)]
		elif num_possibilities == 0:
			if len(operators[state]) == 1:
				return get_state_by_start_char(char, previous, [Operator(state, next(iter(operators[state])))])
			elif operators[state] == {1, 2}:
				if previous == None or isinstance(previous, Operator):
					return get_state_by_start_char(char, previous, [Operator(state, 1)])
				else:
					return get_state_by_start_char(char, previous, [Operator(state, 2)])
		else:
			return State.OPERATOR, state + char, []


def tokenize(code):
	try:
		state_type = State.NONE
		state = ''
		result = []
		
		for i, char in enumerate(code):
			state_type, state, result_new = process_state(state_type, state, char, result[-1] if result else None)
			result += result_new
		
		result += process_state(state_type, state, '', result[-1] if result else None)[2]
		
		return result
	except JSSyntaxError as e:
		e.filename = '<string>'
		e.lineno = code.count('\n', 0, i) + 1
		e.offset = code.find('\n', i) - i
		e.text = code[code.rfind('\n', 0, i) + 1: e.offset]
		raise


if __name__ == '__main__':
	while True:
		try:
			print(*tokenize(input('> ')), sep='\n')
		except JSSyntaxError as e:
			print(e)
