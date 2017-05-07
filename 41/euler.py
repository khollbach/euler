#!/usr/bin/python3

from utils import *

import math

def main():
    test()

    # largest = None
    # n = 2
    # while len(str(n)) <= 9:
        # if n % 1000 == 0:
            # print(n)
        # # Find the next prime.
        # while not is_prime(n):
            # n += 1
        # s = str(n)
        # if is_pan(s):
            # largest = n
        # n += 1
    # print(largest)

    # # Andy's idea.
    # n = 999999999
    # while True:
        # if n % 1000000 == 0:
            # print(n)
        # # if is_pan(str(n)) and is_prime(n):
            # # break
        # #is_pan(str(n))
        # n -= 1
    # print(n)



    for length in range(9, 0, -1):
        s = ''
        for i in range(length):
            s += str(i + 1)

        print(s)
        print(list(s))

        largest = 0
        for p in perms(list(s)):
            x = int(''.join(p))
            if is_prime(x) and x > largest :
                largest = x

        if largest > 0:
            break

    print(largest)

def perms(l):
    '''([object]) -> generator([object])
    Generate all permutations of the list.
    '''
    if len(l) == 0:
        yield []
        return

    for p in perms(l[1:]):
        for i in range(len(p) + 1):
            yield p[:i] + [l[0]] + p[i:]

def is_pan(s):
    '''(str) -> bool
    Is s a permutation of the numbers 1 through len(s)?

    We consider the empty string pandigital.

    O(1)
    '''
    if len(s) > 9:
        return False

    seen = [False] * len(s)
    for c in s:
        offset = ord(c) - ord('1')
        if offset < 0 or offset >= len(s) or seen[offset]:
            return False
        else:
            seen[offset] = True
    return True

def test():
    assert is_pan('123456789')
    assert is_pan('391867254')
    assert not is_pan('3918672540')
    assert not is_pan('0391867254')
    assert not is_pan('3918067254')
    assert not is_pan('391807254')
    assert not is_pan('3918072546')
    assert is_pan('')
    assert is_pan('12')
    assert is_pan('312')
    assert is_pan('3412')
    assert not is_pan('553412')

    import math
    assert len(list(perms(list('12345')))) == math.factorial(5)
    for l in perms(list('12345')):
        print(l)
    for l in perms(list('123456789')):
        pass

if __name__ == '__main__':
    import sys
    sys.exit(main())
