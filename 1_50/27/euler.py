#!/usr/bin/python3

from utils import *

def main():
    most_primes = 39
    product = None

    # The reduced ranges of a and b used here were found by using the value 40
    # to filter out useless pairs.

    a = -100
    while a <= 0:
        b = 0
        while b <= 1000:
            for n in range(80):
                if not is_prime(n**2 + a*n + b):
                    break

            if n > most_primes:
                print(n, a, b)
                most_primes = n
                product = a * b

            b += 1
        a += 1

    print(product)

if __name__ == '__main__':
    import sys
    sys.exit(main())
