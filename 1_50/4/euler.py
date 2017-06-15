#!/usr/bin/python3

# Largest and smallest three digit numbers.
upper_bound = 999
lower_bound = 100

def main():
    largest = 0

    for i in range(upper_bound, lower_bound - 1, -1):
        for j in range(upper_bound, i - 1, -1):
            n = i * j
            if is_pal(str(n)) and n > largest:
                print(i, j, n)
                largest = n

    print('largest: ', largest)

def is_pal(s):
    '''
    Is this string a palindrome?
    '''
    i = 0
    for i in range(len(s)):
        if s[i] != s[-1 - i]:
            return False
    return True

if __name__ == '__main__':
    main()
