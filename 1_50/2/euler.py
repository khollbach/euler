#!/usr/bin/python3

# The largest considered number is 4 million, inclusive.
ulimit = 4000000

def main():
    my_sum = 0

    # Starting from term 2 in the sequence: the second 1.
    i = 2
    while True:
        n = fib(i)
        if n > ulimit:
            break

        if n % 2 == 0:
            print('* ', end='')
            my_sum += n
        print(n)

        i += 1

    print('sum: ', my_sum)

def fib(n):
    if n < 0:
        raise Exception
    elif n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    main()
