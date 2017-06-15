#!/usr/bin/python3

from utils import *

import math

def main():
    # Precompute primality
    is_prime_fast = [False] * 10000
    for i in range(10000):
        if is_prime(i):
            is_prime_fast[i] = True

    for i in range(1000, 10000):
        if is_prime_fast[i]:
            for j in range(i+1, 10000):
                k = j + (j - i)
                if k < 10000 and is_prime_fast[j] and is_prime_fast[k] \
                    and nums_are_perms(i, j) and nums_are_perms(j, k):

                    print(i, j, k)

def nums_are_perms(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import sys
    sys.exit(main())
