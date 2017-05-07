#!/usr/bin/python3

from utils import *

import math

'''
m and n are 'the integer' and 'n' from the question, respectively.
'''

# 5 digits is an easy upper bound on m
limit = 99999

def main():
    test()

    largest = 0

    for m in range(1, limit + 1):
        if m % 1000 == 0:
            print(m)

        tmp = get_pan_product(m)
        if tmp and tmp > largest:
            largest = tmp

    print(largest)

def get_pan_product(m):
    '''(int) -> int
    If m can be made into a pandigital number in the way described in the
    question, then do so and return the concatenated product.
    Otherwise return None.
    '''
    n = 2
    while True:
        s = ''
        for i in range(1, n + 1):
            s += str(m * i)

        if len(s) > 9:
            return None

        if is_pan(s):
            return int(s)

        n += 1

def is_pan(s):
    '''(str) -> bool
    Is s a permutation of the numbers 1 through 9?
    '''
    if len(s) != 9:
        return False
    seen = [False] * 9
    for c in s:
        offset = ord(c) - ord('1')
        if offset < 0 or offset >= 9 or seen[offset]:
            return False
        else:
            seen[offset] = True
    return True

def test():
    assert not is_pan('')
    assert not is_pan('19')
    assert is_pan('123456789')
    assert is_pan('391867254')
    assert not is_pan('391867254 ')
    assert not is_pan(' 391867254')
    assert not is_pan('3918 67254')
    assert not is_pan('3918 7254')

    assert get_pan_product(192) == 192384576
    assert get_pan_product(9) == 918273645
    assert not get_pan_product(123456789)

if __name__ == '__main__':
    import sys
    sys.exit(main())
