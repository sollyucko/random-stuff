from itertools import repeat

from ai import DefinitionAI
from data import words
from random import sample


def get_word_definition_prediction(ai):
	word = sample(words.keys(), k=1)[0]
	definition = sample(words[word], k=1)[0]
	
	prediction = ai.predict(definition)
	
	ai.train(definition, word)
	
	return word, definition, prediction


def ai_result(ai):
	word, definition, prediction = get_word_definition_prediction(ai)
	
	return prediction == word


def main():
	ai = DefinitionAI()
	
	while True:
		word, definition, prediction = get_word_definition_prediction(ai)
		
		print('Definition: ' + definition)
		input('You: ')
		print('AI: ' + prediction)
		print('Answer: ' + word)
		print()
		ai.train(definition, word)


def test():
	ai = DefinitionAI()
	
	while True:
		for i in range(10):
			word, definition, prediction = get_word_definition_prediction(ai)
			
			print(prediction == word, prediction, word)
		
		input()


def ai_quality_test():
	for i in range(10):
		ai = DefinitionAI()
		
		print(sum(map(ai_result, repeat(ai, 100))) / 100)


if __name__ == '__main__':
	main()
	# test()
	# ai_quality_test()
