# Takoma Park Middle School
# Junior 5
# Contest 2
# Solomon Ucko


from collections import Counter
from itertools import groupby
from operator import itemgetter


def main():
    with open('jr-test-input.txt') as in_f:
        sentence = in_f.readline().rstrip('\n')
        print(len(set(filter(str.isalpha, sentence.lower()))), file=out_f)
        print(len(tuple(filter('aeiou'.__contains__, sentence))), file=out_f)
        print(len(tuple(filter(str.isupper, sentence))), file=out_f)
        print(max(Counter(filter(str.isalpha, sentence.lower())).values()), file=out_f)
        # c for c in sentence if c.isalpha() or c == ' ' |> ''.join |> .split() |> sorted$(key=len)
        #  |> groupby$(key=len) |> map$(pair -> (pair[0], tuple(pair[1]))) |> max$(key=$[0]) |> $[1]
        #  |> min$(key=.lower()) |> print$(file=out_f)  # Coconut-like syntax (coconut-lang.org)
        print(
            min(
                max(
                    (
                        (a, tuple(b))
                        for a, b
                        in groupby(
                            sorted(
                                ''.join(
                                    c for c in sentence if c.isalpha() or c == ' '
                                ).split(),
                                key=len
                            ),
                            key=len
                        )
                    ),
                    key=itemgetter(0)
                )[1],
                key=str.lower
            )
        )


if __name__ == '__main__':
    main()
