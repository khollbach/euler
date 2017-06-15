#!/usr/bin/python3

from utils import *

import math

'''
Note: this is a little slow. May take about a minute.
'''

# Inclusive
limit = 1000

def main():
    test()

    best_p = None
    most_solns = 0

    for p in range(1, limit + 1):
        if p % 100 == 0:
            print(p)

        solns = right_triangles(p)
        if len(solns) > most_solns:
            print(p, solns)
            best_p = p
            most_solns = len(solns)

    print(best_p)

def right_triangles(p):
    '''(int) -> [(int,int,int)]
    Return the (integer) right triangles with perimeter p.
    '''
    triangles = []

    # c is always the longest side (hypotenuse)
    for c in range(1, p):
        for b in range(1, min(c, p - c)):
            a = p - b - c
            if a <= 0 or a > b:
                continue

            if a**2 + b**2 == c**2:
                triangles.append((a,b,c))
    return triangles

def test():
    assert right_triangles(120) == [(30,40,50), (24,45,51), (20,48,52)]

if __name__ == '__main__':
    import sys
    sys.exit(main())
