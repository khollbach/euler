#!/usr/bin/python3

from utils import *

def main():
    # Test:
    assert not is_lucky(1, 4)
    assert not is_lucky(666, 4)
    assert is_lucky(1634, 4)
    assert is_lucky(8208, 4)
    assert is_lucky(9474, 4)

    mysum = 0
    for i in range(1000000):
        if is_lucky(i, 5):
            print(i)
            mysum += i

    print('sum:', mysum)

def is_lucky(n, k):
    return n > 1 and n == sum(int(d)**k for d in str(n))

if __name__ == '__main__':
    import sys
    sys.exit(main())
