#!/usr/bin/python3

from utils import *

import math

def main():
    i = 1
    while len(str(fib(i))) < 1000:
        i += 1

    print(i)

fib_cache = {}
def fib(n):
    if n < 1:
        print('n < 1')
        raise Exception

    if n in fib_cache:
        return fib_cache[n]
    elif n == 1 or n == 2:
        return 1
    else:
        tmp = fib(n-1) + fib(n-2)
        fib_cache[n] = tmp
        return tmp

if __name__ == '__main__':
    import sys
    sys.exit(main())
