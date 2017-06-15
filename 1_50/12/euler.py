#!/usr/bin/python3

limit = 500

def main():
    # Loop invariant: n is the i'th triangle number.
    i = 1
    n = 1
    while True:
        how_many = num_divisors(n)
        print(str(i) + ':', str(n) + ',', how_many)
        if how_many > limit:
            break

        i += 1
        n += i

    print(n)

def get_prime_factors(n):
    '''(int) -> {int:int}
    Return the prime factors of n with multiplicities.
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

def num_divisors1(n):
    '''Too slow :('''
    if n < 1:
        return None

    how_many = 0
    for i in range(1, n + 1):
        if n % i == 0:
            how_many += 1
    return how_many

def num_divisors2(n):
    if n < 1:
        return None

    factors = get_prime_factors(n)

    how_many = 1
    for prime in factors:
        how_many *= factors[prime] + 1

    return how_many

num_divisors = num_divisors2

if __name__ == '__main__':
    main()
