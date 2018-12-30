"""Ultra-modular, ultra-functional fizzbuzz."""


from functools import partial


def single(fizz_types, number):
	return ''.join(text for mod, text in fizz_types if number % mod == 0) or str(number)


def multiple(fizz_types, start, end):
	return '\n'.join(map(partial(single, fizz_types), range(start, end + 1)))
	# range(start, end + 1) |> map$(single$(fizz_types)) |> '\n'.join


def main():
	print(multiple([
		(3, 'fizz'),
		(5, 'buzz')
	], 1, 100))


if __name__ == '__main__':
	main()