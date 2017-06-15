#!/usr/bin/python3

from utils import *

import math

def main():
    test()

    count = 0
    for line in open('words.txt'):
        word = line.strip()
        if is_triangle_word(word):
            print(word, count)
            count += 1
    print(count)

def t(n):
    '''(int) -> int
    '''
    assert n > 0
    return n * (n+1) // 2

def is_triangle_word(word):
    '''(str) -> bool
    '''
    charsum = 0
    for c in word:
        charsum += ord(c) - ord('A') + 1

    i = 1
    while True:
        if t(i) == charsum:
            return True
        elif t(i) > charsum:
            return False
        i += 1

    return False

def test():
    assert t(1) == 1
    assert t(2) == 3
    assert t(3) == 6
    assert t(4) == 10
    assert t(5) == 15
    assert t(6) == 21
    assert t(7) == 28
    assert t(8) == 36
    assert t(9) == 45
    assert t(10) == 55

    assert is_triangle_word('SKY')
    assert not is_triangle_word('WORD')

if __name__ == '__main__':
    import sys
    sys.exit(main())
