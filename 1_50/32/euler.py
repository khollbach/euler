#!/usr/bin/python3

from utils import *

# TODO: how to choose a good upper bound?
limit = 10000

def main():
    # Test
    assert not is_pan('')
    assert not is_pan('19')
    assert is_pan('123456789')
    assert is_pan('391867254')
    assert not is_pan('391867254 ')
    assert not is_pan(' 391867254')
    assert not is_pan('3918 67254')
    assert not is_pan('3918 7254')

    mysum = 0
    for i in range(1, limit + 1):
        if i % 1000 == 0:
            print(i)

        divs = get_divisors(i)

        for div in divs:
            if is_pan(str(i) + str(div) + str(i // div)):
                mysum += i
                break

    print(mysum)

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

if __name__ == '__main__':
    import sys
    sys.exit(main())
