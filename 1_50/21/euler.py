#!/usr/bin/python3

# Ten thousand.
limit = 10000

def old_main():
    '''
    Completely misunderstood the def'n of amicable numbers; whoops!
    Let's try this over again. d_value(...) works though!
    '''
    # {int:bool}, mapping from d-values to flags.
    # The flag is false if the origin of this d-value hasn't yet been counted
    # as an amicable number. And true if it has already been counted.
    d_values = {}

    count = 0

    for i in range(1, limit):
        if i % 100 == 0:
            print('i:', i, 'count:', count)

        d = d_value(i)

        if d in d_values:
            # Count the new number.
            count += 1

            # Count the origin of this d-value if we haven't done so yet.
            if not d_values[d]:
                count += 1
                d_values[d] = True
        else:
            d_values[d] = False

    print('count:', count)

def main():
    mysum = 0

    # {number:d_value}
    candidates = {}
    for i in range(1, limit):
        d = d_value(i)

        if d in candidates and candidates[d] == i:
            mysum += i
            mysum += d
        else:
            candidates[i] = d

    print(mysum)

def d_value(n):
    return sum(get_divisors(n)) - n

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
    Return the divisors of n.
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

if __name__ == '__main__':
    main()
