#!/usr/bin/python3



limit = 28123



def main():
    print('divisors of 28:', get_divisors(28))

    print('12 is abundant?', is_abundant(12))

    abundant_numbers = []
    for i in range(1, limit + 1):
        if i % 100 == 0:
            print(i)

        if is_abundant(i):
            abundant_numbers.append(i)

    input()

    for n in abundant_numbers:
        print(n)

    input()

    largest_non_abundant_sum_so_far = 0
    for i in range(1, limit + 1):
        print(i)

        if not is_sum_of_abundant_nums(i, abundant_numbers):
            largest_non_abundant_sum_so_far = i

    print('breakpoint', breakpoint)

def get_prime_factors(n):
    '''(int) -> {int:int}
    Return the prime factors of n with multiplicities.
    Requires n > 0.
    '''
    if n < 1:
        return None

    factors = {}

    i = 2
    while i <= n:
        if n % i == 0:
            # Insert / increment the prime.
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
    '''
    if n < 1:
        return None

    factors = get_prime_factors(n)

    how_many = 1
    for prime in factors:
        how_many *= factors[prime] + 1

    return how_many

def combinations(ranges):
    '''[int] -> generator([int])
    The input list, ranges=[n1,...,nk], is treated as a list of non-inclusive
    upper-bounds. We generate all possible lists [m1,...,mk] such that
    0 <= m1 < n1, ..., 0 <= mk < nk. We generate them in a sensible order:
    the numbers further to the right in the list vary most rapidly.
    '''
    # Base case
    if len(ranges) == 0:
        yield []
        return

    for i in range(ranges[0]):
        for combo in combinations(ranges[1:]):
            yield [i] + combo

def get_divisors(n):
    '''(int) -> {int}
    Return the divisors of n, returned as a list.
    1 is the first in the list, n is the last in the list.
    There are no other guarantees on the order of the list.
    Requires n > 0.
    '''
    if n < 1:
        return None

    # [(int, int)]; first is prime factor, second is multiplicity.
    factor_list = []
    factors = get_prime_factors(n)
    for fact in factors:
        factor_list.append((fact, factors[fact]))

    # Inclusive ranges [[0..mult_1], ..., [0..mult_k]],
    # represented as a list of non-inclusive upper bounds.
    ranges = [mult + 1 for fact, mult in factor_list]

    # Compute divisors of n.
    divisors = set()
    for combo in combinations(ranges):
        divisor = 1
        for i in range(len(factor_list)):
            divisor *= factor_list[i][0] ** combo[i]
        divisors.add(divisor)

    return divisors



def sum_of_proper_divisors(n):
    divisors = get_divisors(n)

    # Sum of divisors
    temp_sum = sum(divisors)

    return temp_sum - n

def is_deficient(n):
    return sum_of_proper_divisors(n) < n

def is_abundant(n):
    return sum_of_proper_divisors(n) > n

def is_perfect(n):
    return sum_of_proper_divisors(n) == n

def pairs():
    '''
    Generate all pairs of numbers.
    '''
    # TODO
    pass

def is_sum_of_abundant_nums(n, abundant_numbers):
    #for i in abundant_numbers:
    #    for j in abundant_numbers:
    #        if n == i + j:
    #            return True
    #        elif i > n or j > n:
    #            return False
    #return False

    # TODO: iterate over all pairs, breaking when we exceed n.
    pass


if __name__ == '__main__':
    main()
