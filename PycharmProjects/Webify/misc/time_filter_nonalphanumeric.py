from inspect import getsource
from random import sample
import re
from string import printable
from timeit import timeit

pattern_single = re.compile(r'[\W]')
pattern_repeat = re.compile(r'[\W]+')
translation_tb = str.maketrans('', '', ''.join(c for c in map(chr, range(256)) if not c.isalnum()))


def generate_test_string(length):
    return ''.join(sample(printable, length))


def main():
    for i in range(0, 60, 10):
        for test in [
            lambda: ''.join(c for c in generate_test_string(i) if c.isalnum()),
            lambda: ''.join(filter(str.isalnum, generate_test_string(i))),
            lambda: re.sub(r'[\W]', '', generate_test_string(i)),
            lambda: re.sub(r'[\W]+', '', generate_test_string(i)),
            lambda: pattern_single.sub('', generate_test_string(i)),
            lambda: pattern_repeat.sub('', generate_test_string(i)),
            lambda: generate_test_string(i).translate(translation_tb),

        ]:
            print('', timeit(test), i, getsource(test).lstrip('            lambda: ').rstrip(',\n'), sep='\t')


if __name__ == '__main__':
    main()
