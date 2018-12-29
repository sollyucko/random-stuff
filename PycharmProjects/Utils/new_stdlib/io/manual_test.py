from new_stdlib.io import wrap_file_object


def main():
    file = wrap_file_object(open('test.txt', 'w'))
    print(file)
    file.write('abc')
    file.close()


if __name__ == '__main__':
    main()
