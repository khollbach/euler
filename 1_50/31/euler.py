#!/usr/bin/python3

from utils import *

def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    def make_change(n):
        return change(n, coins)

    assert make_change(0) == 1
    assert make_change(1) == 1
    assert make_change(2) == 2
    assert make_change(3) == 2
    assert make_change(4) == 3
    assert make_change(5) == 4

    print(make_change(200))

# Number of ways to make change.
def change(n, coins):
    if n < 0:
        print('n < 0')
        raise Exception
    if n == 0:
        return 1
    if len(coins) == 0:
        return 0

    ways = 0
    if coins[-1] <= n:
        ways += change(n - coins[-1], coins)
    ways += change(n, coins[:-1])

    return ways

if __name__ == '__main__':
    import sys
    sys.exit(main())
