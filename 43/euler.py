#!/usr/bin/python3

from utils import *

import math

def main():
    test()

    mysum = 0
    for l in permutations(list('1234567890')):
        s = ''.join(l)
        if s[0] == '0':
            continue
        n = int(s)
        if interesting(n):
            mysum += n
            print(n, mysum)
    print(mysum)

def zero_to_nine_pan(n):
    '''(int) -> bool
    '''
    s = str(n)
    if len(s) != 10:
        return False

    seen = [False] * 10
    for c in s:
        offset = ord(c) - ord('0')
        if offset < 0 or offset >= 10 or seen[offset]:
            return False
        else:
            seen[offset] = True
    return True

divisors = [None, None, 2, 3, 5, 7, 11, 13, 17]
def interesting(n):
    '''(int) -> bool
    '''
    s = str(n)
    if len(s) != 10:
        return False

    s = ' ' + s  # Indices start from 1
    for i in range(2, 8 + 1):
        if int(s[i:i+3]) % divisors[i] != 0:
            return False
    return True

def test():
    assert zero_to_nine_pan(1406357289)
    assert not zero_to_nine_pan(146357289)

    assert interesting(1406357289)
    assert not interesting(1406357298)

if __name__ == '__main__':
    import sys
    sys.exit(main())
