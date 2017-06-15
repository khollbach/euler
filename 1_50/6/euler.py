#!/usr/bin/python3

# Both inclusive.
lower_bound = 1
upper_bound = 100

def main():
    # Sum of squares.
    sum1 = 0
    for i in range(lower_bound, upper_bound + 1):
        sum1 += i ** 2

    print('sum1:', sum1)

    # Square of sums.
    sum2 = 0
    for i in range(lower_bound, upper_bound + 1):
        sum2 += i
    sum2 **= 2

    print('sum2:', sum2)

    print('difference:', sum2 - sum1)

if __name__ == '__main__':
    main()
