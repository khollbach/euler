#!/usr/bin/python3

from utils import *

import math

def main():
    test()

    product = 1

    i = 1
    n = 1
    power = 0
    while power <= 6:
        s = str(n)
        offset = 10**power - i
        if 0 <= offset < len(s):
            product *= int(s[offset])
            power += 1

        i += len(s)
        n += 1

    print(product)

def test():
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main())
