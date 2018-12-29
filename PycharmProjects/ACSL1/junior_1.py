def main():
    for f in (len,
              lambda x: sum(map(int, x)),
              lambda x: sum(int(d) for i, d in enumerate(x) if i % 2 == 0),
              lambda x: x.count('4'),
              lambda x: x[(len(x) - 1) // 2]):
        print(f(input('> ')))


if __name__ == '__main__':
    main()
