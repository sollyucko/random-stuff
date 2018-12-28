from .common import EndParen, StartParen


def generate_paren_tree(token_list):
	return list(_generate_paren_tree(iter(token_list)))


def _generate_paren_tree(token_iterable):
	for token in token_iterable:
		if isinstance(token, StartParen):
			yield list(_generate_paren_tree(token_iterable))
		elif isinstance(token, EndParen):
			break
		else:
			yield token
