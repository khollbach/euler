#!/usr/bin/python3

lower_bound = 1
upper_bound = 20

def main():
    factors = {}
    for i in range(lower_bound, upper_bound + 1):
        some_factors = get_prime_factors(i)
        for p in some_factors:
            if not p in factors or factors[p] < some_factors[p]:
                factors[p] = some_factors[p]

    print('factors:', factors)
    
    number = 1
    for p in factors:
        number *= p ** factors[p]

    print('number:', number)

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

if __name__ == '__main__':
    main()
