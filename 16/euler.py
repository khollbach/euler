#!/usr/bin/python3

def main():
    big_number = 2**1000
    string = str(big_number)

    digit_sum = 0
    for c in string:
        digit_sum += int(c)

    print(digit_sum)

if __name__ == '__main__':
    main()
