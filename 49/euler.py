#!/usr/bin/python3

from utils import *

import math

def main():
    # Precompute primality
    is_prime_fast = [False] * 10000
    for i in range(10000):
        if is_prime(i):
            is_prime_fast[i] = True

    # TODO

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import sys
    sys.exit(main())
