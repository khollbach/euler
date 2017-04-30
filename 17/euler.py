#!/usr/bin/python3 

digit_strings = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

multiple_of_ten_strings = [
    'zero',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]

teen_strings = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

def main():
    num_letters = 0
    for i in range(1, 1001):
        english = num_to_english(i)

        # Magic number = 40?
        padding = ''.join([' '] * (40 - len(english)))
        print(english, end=padding)

        english = english.replace(' ', '').replace('-', '')
        print(english)

        num_letters += len(english)

    print(num_letters)

def num_to_english(n):
    '''(int) -> str
    '''
    if n < 0:
        raise Exception('NYI')
    elif n == 0:
        return digit_strings[0]

    digits = [int(d) for d in str(n)]

    english = ''
    for i in range(len(digits)):
        trailing_zeros = len(digits) - 1 - i

        if digits[i] == 0:
            continue

        # Add separator (usually whitespace).
        if i > 0:
            # Special case: multiples of ten.
            if trailing_zeros == 1:
                english += ' and '
            # Special case: ones digit.
            elif trailing_zeros == 0:
                # Eg: one hundred and one
                if digits[i-1] == 0:
                    english += ' and '
                # Eg: twenty-two
                else:
                    english += '-'
            else:
                english += ' '

        # Special case: teens.
        if trailing_zeros == 1 and digits[i] == 1:
            english += teen_strings[digits[i+1]]
            break

        english += decimal_place_to_string(digits[i], trailing_zeros)

    return english

def decimal_place_to_string(digit, trailing_zeros):
    '''(int, int) -> str
    Takes a single decimal digit number and a number of trailing zeros (ie
    the decimal place).

    Returns the english language string corresponding to the number
    dig * 10**trailing_zeros.

    Eg: (5, 00) -> 'five hundred'

    Very incomplete; YMMV.
    '''
    if trailing_zeros < 0:
        raise Exception('NYI')
    elif trailing_zeros == 0:
        return digit_strings[digit]
    elif trailing_zeros == 1:
        return multiple_of_ten_strings[digit]
    elif trailing_zeros == 2:
        return digit_strings[digit] + ' hundred'
    elif trailing_zeros == 3:
        return digit_strings[digit] + ' thousand'
    else:
        raise Exception('NYI')

if __name__ == '__main__':
    main()
