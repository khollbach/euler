#!/usr/bin/python3

from utils import *

import math

def main():
    test()

    mysum = 0

    count = 0  # We know we're done once we hit 11.
    n = 10     # We don't consider single-digit numbers, as per the question.
    while count < 11:
        if n % 1000 == 0:
            print(n)

        if is_trunc_prime(n):
            mysum += n
            count += 1
        n += 1

    print()
    print(mysum)

def is_trunc_prime(n):
    '''(int) -> bool
    Is n a truncatable prime?
    '''
    s = str(n)
    # We reverse it for speed: checking small numbers for primality is easier.
    for i in reversed(range(len(s))):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
            return False
    return True

def test():
    assert not is_trunc_prime(0)
    assert not is_trunc_prime(1)
    assert is_trunc_prime(2)
    assert is_trunc_prime(3)
    assert not is_trunc_prime(4)
    assert is_trunc_prime(5)
    assert is_trunc_prime(3797)
    assert not is_trunc_prime(3777)

if __name__ == '__main__':
    import sys
    sys.exit(main())
