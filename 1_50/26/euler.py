#!/usr/bin/python3

from utils import *

import math

def main():
    limit = 1000

    d = None
    max_length = 0

    for n in range(2, limit):
        decimals = []
        seen_ms = []

        # How long is the repeating string of digits? (if any)
        length = 0

        ## Long division.
        # Exit once there is no remainder.
        m = 1
        while m != 0:
            # Shift until n goes into m
            while n > m:
                m *= 10

            # If we reach an m we've seen before, things will repeat.
            if m in seen_ms:
                # How long ago did we see this m?
                length = len(seen_ms) - seen_ms.index(m)
                break
            seen_ms.append(m)

            # How many times does n go into m?
            decimals.append(m // n)

            # Remainder?
            m = m % n

        if length > max_length:
            d = n
            max_length = length

        print(n, length, decimals)

    print(d, max_length)

if __name__ == '__main__':
    import sys
    sys.exit(main())
