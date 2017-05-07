#!/usr/bin/python3

from utils import *

import math

# One million, non-inclusive.
limit = 1000000

def main():
    test()

    mysum = 0
    for i in range(limit):
        if is_pal(str(i)) and is_pal(bin_str(i)):
            mysum += i
    print(mysum)

def is_pal(s):
    '''(str) -> bool
    Is this string a palindrome?
    '''
    i = 0
    for i in range(len(s)):
        if s[i] != s[-1 - i]:
            return False
    return True

def bin_str(n):
    '''(int) -> str
    Return the binary string representation of n, with out leading zeros
    unless n==0, in which case there is one leading zero.
    '''
    if n < 0:
        raise Exception('NYI')
    if n == 0:
        return '0'

    s = ''
    while n != 0:
        s = str(n % 2) + s
        n //= 2

    return s

def test():
    assert bin_str(0) == '0'
    assert bin_str(1) == '1'
    assert bin_str(2) == '10'
    assert bin_str(585) == '1001001001'

if __name__ == '__main__':
    import sys
    sys.exit(main())
