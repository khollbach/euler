#!/usr/bin/python3

from utils import *

# Anything larger than this is guaranteed to be an ab-sum.
limit = 28123

def main():
    ab_nums_gen = abundant_numbers()
    ab_nums_list = []

    ab_sums = set()

    # Iterate thru all pairs (i,j) as indices to ab_nums_list
    i = 0
    while True:
        # See how far along we are. I tried it and it takes about i=7000.
        if i % 100 == 0:
            print(i)

        ab_nums_list.append(next(ab_nums_gen))

        j = 0
        while j <= i:
            # Add another ab_sum to the set.
            num = ab_nums_list[i] + ab_nums_list[j]
            ab_sums.add(num)

            j += 1

        # If the i'th ab-num itself is larger than the limit,
        # we're for sure done.
        # (We could check n+12>limit but this is fine.)
        if ab_nums_list[i] > limit:
            break

        i += 1

    # Calculate the sum of all numbers that are not 'abundant sums'.
    mysum = 0
    for i in range(1, limit + 1):
        if i not in ab_sums:
            mysum += i

    print('sum:', mysum)

def sum_of_proper_divisors(n):
    '''(int) -> int
    Return the sum of the proper divisors of n.
    Requires n > 0.
    '''
    if n < 1:
        return None

    divisors = get_divisors(n)

    # Sum of divisors
    temp_sum = sum(divisors)

    return temp_sum - n

def pairs_of_naturals():
    '''() -> generator:(int,int)
    Generate all pairs of natural numbers.
    '''
    i = 0
    while True:
        j = 0
        while j <= i:
            yield i, j
            j += 1
        i += 1

def abundant_numbers():
    '''() -> generator:int
    Generate all abundant_numbers.
    '''
    i = 1
    while True:
        if sum_of_proper_divisors(i) > i:
            yield i
        i += 1

if __name__ == '__main__':
    main()
