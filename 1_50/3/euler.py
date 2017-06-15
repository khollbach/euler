#!/usr/bin/python3

limit = 600851475143

def main():
    n = limit
    largest = None

    i = 2
    while i <= n:
        # If it's a prime factor, divide it out.
        if is_prime(i) and n % i == 0:
            print(i)
            largest = i
            n //= i
        else:
            i += 1

    print('largest: ', largest)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
