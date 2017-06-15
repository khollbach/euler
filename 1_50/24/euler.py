#!/usr/bin/python3

from utils import *

import math

def main():
    print(nth_perm(999999, list(range(10))))

def nth_perm(n, l):
    '''
    n starts from 0.
    '''
    print(n, l)

    if n < 0:
        print('n < 0')
        return None
    if n >= math.factorial(len(l)):
        print('n too large')
        return None

    if n == 0:
        return l

    fact = math.factorial(len(l) - 1)

    # Find the largest number N s.t. N*fact <= n
    for N in range(len(l)):
        if N*fact > n:
            N -= 1
            break

    assert N*fact <= n

    # Pull the N'th number to the front and recurse on the rest.
    return [l.pop(N)] + nth_perm(n - N*fact, l)

if __name__ == '__main__':
    import sys
    sys.exit(main())
