#!/usr/bin/python3

from utils import *

import math

N = 1000

def main():
    mysum = 0
    for i in range(1, N+1):
        mysum += i ** i
    print(str(mysum)[-10:])

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import sys
    sys.exit(main())
