#!/usr/bin/python3

from utils import *

def main():
    seen = set()

    for a in range(2, 100 + 1):
        for b in range(2, 100 + 1):
            seen.add(a**b)

    print(len(seen))

if __name__ == '__main__':
    import sys
    sys.exit(main())
