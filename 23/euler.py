#!/usr/bin/python3

from utils import *

# Inclusive.
limit = 28123

def main():
    # Calculate abundant numbers.
    abundant_numbers = set()
    for i in range(1, limit + 1):
        if i % 100 == 0:
            print(i)

        if sum_of_proper_divisors(i) > i:
            abundant_numbers.add(i)

    # Calculate largest number that is not an 'abundant sum'.
    largest = 0
    for i in range(1, limit + 1):
        if i % 100 == 0:
            print(i)

        if not is_abundant_sum(i, abundant_numbers):
            largest = i

    print('largest:', largest)

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

def is_abundant_sum(n, abundant_numbers):
    '''(int, {int}) -> bool
    Can n be written as a sum of two abundant numbers?
    Takes a set of abundant numbers as input,
    the set must contain all abundant numbers smaller than n.
    '''
    if n < 2:
        return False

    return True  # TODO

if __name__ == '__main__':
    main()
