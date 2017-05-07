#!/usr/bin/python3

from utils import *

import math

'''
Warning: this implementation is VERY SLOW!
Takes a couple of minutes to run. Not more than 5.

Should instead use an array of length one million methinks.
'''

# One million. Non-inclusive.
limit = 1000000

def main():
    test()

    count = 0
    for n in range(limit):
        if n % 1000 == 0:
            print(n)

        if circ_prime(n):
            count += 1
    print('count:', count)

def circ_prime(n):
    '''(int) -> bool
    '''
    def rotations(n):
        s = str(n)
        for i in range(len(s)):
            yield int(s[i:] + s[:i])

    for i in rotations(n):
        if not is_prime(i):
            return False
    return True

def test():
    assert not circ_prime(0)
    assert not circ_prime(1)
    assert circ_prime(2)
    assert circ_prime(3)
    assert not circ_prime(4)
    assert circ_prime(5)
    assert not circ_prime(6)
    assert circ_prime(7)
    assert circ_prime(11)
    assert circ_prime(13)
    assert circ_prime(17)
    assert not circ_prime(19)
    assert not circ_prime(23)
    assert not circ_prime(29)
    assert circ_prime(31)

if __name__ == '__main__':
    import sys
    sys.exit(main())
