#!/usr/bin/python3

'''
Helper functions for Project Euler problems.
Mostly to do with prime numbers and the like.
'''

import math

fib_cache = {}
def fib(n):
    '''(int) -> int
    n'th Fibonacci number, where fib(0) == 0 and fib(1) == 1

    TODO: runtime?
        (Make it better with DP?)
    '''
    if n < 0:
        print('n < 0')
        raise Exception

    if n in fib_cache:
        return fib_cache[n]
    elif n == 0 or n == 1:
        return n
    else:
        tmp = fib(n-1) + fib(n-2)
        fib_cache[n] = tmp
        return tmp

def is_prime(n):
    '''(int) -> bool
    Is n prime?

    O(sqrt(n))
    '''
    if n < 2:
        return False

    m = math.sqrt(n)

    i = 2
    while i <= m + 0.1:
        if n % i == 0:
            return False
        i += 1
    return True

def get_prime_factors(n):
    '''(int) -> {int:int}
    Return the prime factors of n with multiplicities.
    Requires n > 0.

    O(n)
    '''
    if n < 1:
        return None

    factors = {}

    i = 2
    while i <= n:
        if n % i == 0:
            # Insert the prime / increment its multiplicity.
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1

            # Divide it out.
            n //= i
        else:
            i += 1

    return factors

def get_num_divisors(n):
    '''(int) -> int
    Return the number of divisors of n.
    Requires n > 0.

    O(n)
    '''
    if n < 1:
        return None

    factors = get_prime_factors(n)

    how_many = 1
    for prime in factors:
        how_many *= factors[prime] + 1

    return how_many

def get_divisors(n):
    '''(int) -> {int}
    Return the divisors of n.
    Requires n > 0.

    O(n)
    '''
    if n < 1:
        return None

    # [(int, int)]; first is prime factor, second is multiplicity.
    factor_list = []
    factors = get_prime_factors(n)
    for prime in factors:
        factor_list.append((prime, factors[prime]))

    # Inclusive ranges [[0..mult_1], ..., [0..mult_k]],
    # represented as a list of non-inclusive upper bounds.
    ranges = [mult + 1 for fact, mult in factor_list]

    # Helper function.
    def combinations(ranges):
        '''[int] -> generator([int])
        The input list, ranges=[n1,...,nk], is treated as a list of
        non-inclusive upper-bounds.

        We generate all possible lists [m1,...,mk] such that
        0 <= m1 < n1, ..., 0 <= mk < nk.

        We generate them in a sensible order:
        the numbers further to the right in the list vary most rapidly.

        This is O(n), where n is the product of the m_i's.
        '''
        # Base case
        if len(ranges) == 0:
            yield []
            return

        for i in range(ranges[0]):
            for combo in combinations(ranges[1:]):
                yield [i] + combo

    # Compute divisors of n.
    # Each distinct combination of multiplicities (ie exponents) of its prime
    # factors defines a distinct divisor.
    divisors = set()
    for combo in combinations(ranges):
        # Take the product of the prime factors to their exponents.
        divisor = 1
        for i in range(len(factor_list)):
            divisor *= factor_list[i][0] ** combo[i]
        divisors.add(divisor)

    return divisors

def simplest_terms(n, m):
    '''(int, int) -> (int, int)
    Reduce a fraction to simplest terms.

    O(n + m)
    '''
    from collections import Counter
    from functools import reduce

    n_factors = Counter(get_prime_factors(n))
    m_factors = Counter(get_prime_factors(m))

    n_factors, m_factors = n_factors - m_factors, m_factors - n_factors

    numerator = reduce(int.__mul__, [f for f in n_factors.elements()], 1)
    denomenator = reduce(int.__mul__, [f for f in m_factors.elements()], 1)

    return numerator, denomenator

def permutations(l):
    '''([object]) -> generator([object])
    Generate all permutations of the list.
    '''
    if len(l) == 0:
        yield []
        return

    for p in permutations(l[1:]):
        for i in range(len(p) + 1):
            yield p[:i] + [l[0]] + p[i:]
