#!/usr/bin/python3

from utils import *

def main():
    print(funk(1001))

def funk(n):
    '''(int) -> int, int
    Return the sum, and also the largest number (ie top-right diagonal).
    '''
    if n < 0:
        print('n should be positive')
        print(n)
        raise Exception
    if n % 2 == 0:
        print('n should be odd')
        print(n)
        raise Exception

    if n == 1:
        return 1, 1

    prevsum, topright = funk(n - 2)

    newsum = prevsum
    for i in range(1, 5):
        newsum += topright + i * (n-1)

    return newsum, topright + 4 * (n-1)

if __name__ == '__main__':
    import sys
    sys.exit(main())
