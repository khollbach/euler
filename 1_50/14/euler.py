#!/usr/bin/python3

# One million
limit = 1000000

def main():
    longest = 0
    number = None

    for i in range(1, limit):
        length = collatz_length(i)
        if length > longest:
            print(i, length)
            longest = length
            number = i

    print(number)

collatz_cache = {}
def collatz_length(n):
    if n < 1:
        return None
    elif n == 1:
        return 1
    elif n in collatz_cache:
        return collatz_cache[n]
    elif n % 2 == 0:
        length = collatz_length(n // 2) + 1
        collatz_cache[n] = length
        return length
    else:
        length = collatz_length(3 * n + 1) + 1
        collatz_cache[n] = length
        return length

if __name__ == '__main__':
    main()
