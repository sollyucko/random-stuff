from collections import Counter
from itertools import product
from typing import DefaultDict

from spacy import load


nlp = load('en_core_web_sm')


def similarity(pair):
	first, second = pair
	
	try:
		result = first.similarity(second)
	except TypeError:
		print(repr(first), repr(second))
		raise
	
	return result


def calculate_score(token_set_1, token_set_2):
	result = sum(
		map(
			lambda score: 0 if score == 1 else 1,
			map(
				similarity,
				# lambda pair: pair[0].similarity(pair[1]),
				product(token_set_1, token_set_2)
			)
		)
	) / len(token_set_1) / len(token_set_2)
	
	# print(result)
	
	return result


class DefinitionAI:
	def __init__(self):
		self.outputs = DefaultDict(Counter)
	
	def predict(self, inp: str) -> str:
		input_tokens = nlp(inp)
		
		try:
			return max({(output, calculate_score(input_tokens, output_tokens)) for (output, output_tokens) in self.outputs.items()}, key=lambda value: value[1])[0]
		except ValueError:
			return "I don't know"
	
	def train(self, inp: str, out: str):
		new_tokens = set(nlp(inp)) | set(nlp(out))
		
		self.outputs[out] += Counter(filter(lambda token: len(str(token)) > 1, new_tokens))
