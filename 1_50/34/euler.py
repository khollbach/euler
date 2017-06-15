#!/usr/bin/python3

from utils import *

import math

# TODO: how to find a good upper limit?
lower = 3
upper = 1000000

def main():
    nums = []
    for n in range(lower, upper):
        if n % 1000 == 0:
            print(n)

        if sum(math.factorial(int(d)) for d in str(n)) == n:
            print(n)
            nums += [n]

    print(sum(nums))

if __name__ == '__main__':
    import sys
    sys.exit(main())
