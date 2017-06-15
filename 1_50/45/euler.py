#!/usr/bin/python3

from utils import *

import math

def main():
    n = 1
    while True:
        hn = h(n)
        if is_tri(hn) and is_pent(hn):
            print(n, hn)

        n += 1

def t(n):
    '''(int) -> int
    nth triangle number.

    O(1)

    >>> t(1)
    1
    >>> t(2)
    3
    >>> t(3)
    6
    >>> t(4)
    10
    >>> t(5)
    15
    '''
    return n * (n + 1) // 2

def p(n):
    '''(int) -> int
    nth pentagonal number.

    O(1)

    >>> p(1)
    1
    >>> p(2)
    5
    >>> p(3)
    12
    >>> p(4)
    22
    >>> p(5)
    35
    >>> p(6)
    51
    >>> p(7)
    70
    >>> p(8)
    92
    >>> p(9)
    117
    >>> p(10)
    145
    '''
    return n * (3*n - 1) // 2

def h(n):
    '''(int) -> int
    nth hexagonal number.

    O(1)

    >>> h(1)
    1
    >>> h(2)
    6
    >>> h(3)
    15
    >>> h(4)
    28
    >>> h(5)
    45
    '''
    return n * (2*n - 1)

def is_pent(x):
    '''(int) -> int
    Is x a pentagonal number?
    If yes, return the n for which x equals P[n].
    Otherwise return None.

    O(1)

    >>> is_pent(-1)
    >>> is_pent(0)
    >>> is_pent(2)
    >>> is_pent(3)
    >>> is_pent(6)
    >>> is_pent(15)
    >>> is_pent(100)
    >>> is_pent(1)
    1
    >>> is_pent(5)
    2
    >>> is_pent(12)
    3
    >>> is_pent(22)
    4
    >>> is_pent(35)
    5
    >>> is_pent(51)
    6
    >>> is_pent(70)
    7
    >>> is_pent(92)
    8
    >>> is_pent(117)
    9
    >>> is_pent(145)
    10
    '''
    if x < 1:
        return None

    solns = int_solve_quadratic(3, -1, -2 * x)

    # Take only positive solutions.
    def posve(x):
        return x > 0
    solns = list(filter(posve, solns))

    assert len(solns) < 2

    if len(solns) == 0:
        return None
    else:
        return solns[0]

def is_tri(x):
    '''(int) -> int
    Is x a triangle number?
    If yes, return the n for which x equals T[n].
    Otherwise return None.

    O(1)

    >>> is_tri(-1)
    >>> is_tri(0)
    >>> is_tri(2)
    >>> is_tri(50)
    >>> is_tri(100)
    >>> is_tri(1)
    1
    >>> is_tri(3)
    2
    >>> is_tri(6)
    3
    >>> is_tri(10)
    4
    >>> is_tri(15)
    5
    '''
    if x < 1:
        return None

    solns = int_solve_quadratic(1, 1, -2 * x)

    # Take only positive solutions.
    def posve(x):
        return x > 0
    solns = list(filter(posve, solns))

    assert len(solns) < 2

    if len(solns) == 0:
        return None
    else:
        return solns[0]

def is_hex(x):
    '''(int) -> int
    Is x a triangle number?
    If yes, return the n for which x equals T[n].
    Otherwise return None.

    O(1)

    >>> is_hex(-1)
    >>> is_hex(0)
    >>> is_hex(2)
    >>> is_hex(50)
    >>> is_hex(100)
    >>> is_hex(1)
    1
    >>> is_hex(6)
    2
    >>> is_hex(15)
    3
    >>> is_hex(28)
    4
    >>> is_hex(45)
    5
    '''
    if x < 1:
        return None

    solns = int_solve_quadratic(2, -1, -1 * x)

    # Take only positive solutions.
    def posve(x):
        return x > 0
    solns = list(filter(posve, solns))

    assert len(solns) < 2

    if len(solns) == 0:
        return None
    else:
        return solns[0]

def int_solve_quadratic(a, b, c):
    '''(int, int, int) -> [int]
    Solve a quadratic equation with integer coefficients.

    Return a list of the *integer* roots.
    The list will have length 0, 1, or 2.

    O(1)
    '''
    discrim = b**2 - 4*a*c
    if discrim < 0:
        return []

    sqrt = int_sqrt(discrim)
    if sqrt is None:
        return []

    solns = []
    if (-b + sqrt) % (2*a) == 0:
        solns.append((-b + sqrt) // (2*a))
    if sqrt != 0 and (-b - sqrt) % (2*a) == 0:
        solns.append((-b - sqrt) // (2*a))

    return solns

def int_sqrt(n):
    '''(int) -> int
    If n is a perfect square, return the square root of n.
    Otherwise return None.

    O(1)

    >>> int_sqrt(0)
    0
    >>> int_sqrt(1)
    1
    >>> int_sqrt(2)
    >>> int_sqrt(3)
    >>> int_sqrt(4)
    2
    >>> int_sqrt(36)
    6
    '''
    m = math.sqrt(n)
    floor, ceil = math.floor(m), math.ceil(m)
    if floor ** 2 == n:
        return floor
    elif ceil ** 2 == n:
        return ceil
    else:
        return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import sys
    sys.exit(main())
