#!/usr/bin/python3

from utils import *

import math

def main():
    n = 9
    while True:
        if not is_prime(n):
            if not is_sum_of_prime_and_twice_square(n):
                print(n)
                break

        n += 2

def is_sum_of_prime_and_twice_square(n):
    x = 1
    twice_x_squared = 2 * x**2
    while twice_x_squared < n:
        if is_prime(n - twice_x_squared):
            return True

        x += 1
        twice_x_squared = 2 * x**2

    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import sys
    sys.exit(main())
