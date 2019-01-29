from collections import deque


def windowed(iterable, size):
    iterator = iter(iterable)
    d = deque(maxlen=size)
    
    while len(d) < size:
        d.append(next(iterator))
    
    while True:
        yield d
    
        try:
            d.append(next(iterator))
        except StopIteration:
            return


def main():
    for i in range(5):
        a, b = input('> ').split()
        print(sum(map(int, map(''.join, windowed(a, int(b))))))


if __name__ == '__main__':
    main()

# > 1325678905 2
# 455
# > 54981230845791 5
# 489210
# > 4837261529387456 3
# 7668
# > 385018427388713440 4
# 75610
# > 623387770165388734 11
# 471035012254
