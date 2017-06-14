#!/usr/bin/python3

from utils import *

import math

N = 4

def main2():
    '''
    Very slow! (4m56s)
    '''
    n = 1
    while True:
        if n % 1000 == 0:
            print(n)

        for i in range(N):
            if num_distinct_prime_factors(n + i) != N:
                break
        else:
            print(n)
            break

        n += 1

def num_distinct_prime_factors(n):
    return len(get_prime_factors(n))

def main3():
    '''
    Extremely slow also.
    '''
    count = 0
    n = 1
    while True:
        if n % 1000 == 0:
            print(n)

        if num_distinct_prime_factors(n) == N:
            count += 1
            if count == N:
                print(n - N + 1)
                break
        else:
            count = 0

        n += 1

def main():
    '''
    TODO: jump in fours, roughly. This will speed things up a lot.
    '''
    print('NYI')

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import sys
    sys.exit(main())
