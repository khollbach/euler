#!/usr/bin/python3

from utils import *

import math

def main():
    i = 1
    while len(str(fib(i))) < 1000:
        i += 1

    print(i)

if __name__ == '__main__':
    import sys
    sys.exit(main())
