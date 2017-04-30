#!/usr/bin/python3

import math

big_number = 100

def main():
    n = math.factorial(big_number)
    s = str(n)

    mysum = 0
    for c in s:
        mysum += int(c)

    print(mysum, 'lol')

if __name__ == '__main__':
    main()
