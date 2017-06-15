#!/usr/bin/python3

import math

# Two million.
limit = 2000000

def main():
    mysum = 0
    for i in range(limit):
        if is_prime(i):
            print(i)
            mysum += i

    print(mysum)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
