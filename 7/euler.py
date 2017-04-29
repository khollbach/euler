#!/usr/bin/python3

# Ten thousand and one.
which_prime = 10001

def main():
    # How many have we seen so far?
    so_far = 0

    i = 0
    while True:
        if is_prime(i):
            so_far += 1

            print(so_far, i)

            if so_far == which_prime:
                break
        i += 1

    print(i)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
