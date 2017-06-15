#!/usr/bin/python3

from utils import *

import math

def main():
    limit = 1000000  # One million

    # Calculate upper bound on sequence length,
    # and compute a list of that many primes.
    primes = []
    mysum = 0
    i = 0
    while mysum < limit:
        if is_prime(i):
            primes.append(i)
            mysum += i

        i += 1

    print(len(primes))  # 547

    # For each sequence length, look for a prime.
    for sequence_len in range(len(primes), -1, -1):

        mysum = sum(primes[:sequence_len])

        i = 0
        while mysum < limit:
            if is_prime(mysum):
                print(sequence_len, mysum)
                return

            mysum -= primes[i]
            mysum += primes[i + sequence_len]
            i += 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import sys
    sys.exit(main())
