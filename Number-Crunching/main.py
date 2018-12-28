import traceback

from cmymath import primes, save_cache


def main():
    # while True:
    # 	print(next(islice(primes, int(input('> ')), None)))
    # 	# print(prime_factor(int(input('> '))))
    
    for i, p in enumerate(primes):
        if i % 100000 == 0:
            print(i, p)
            save_cache()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        raise
    finally:
        print('Exiting')
        exit()  # Ensure clean exit to call atexit listeners
