#!/usr/bin/python3

from utils import *

# Both inclusive
lower = 10
upper = 99

def main():
    assert fracs_equal(30, 50, 3, 5)
    assert fracs_equal(49, 98, 4, 8)
    assert not fracs_equal(51, 98, 4, 8)

    digit_cancelling_fracs = []
    for m in range(lower, upper + 1):
        for n in range(lower, m):
            if n == m:
                continue

            # Lists of strings
            ln = list(str(n))
            lm = list(str(m))

            if ln[1] == lm[1] == '0':
                continue
            
            digit_cancelling = False
            for i in range(2):
                for j in range(2):
                    if ln[i] == lm[j]:
                        n2 = int(''.join(ln[:i] + ln[i+1:]))
                        m2 = int(''.join(lm[:j] + lm[j+1:]))
                        if m2 != 0 and fracs_equal(n, m, n2, m2):
                            digit_cancelling = True
            if digit_cancelling:
                print(n, m)
                digit_cancelling_fracs.append((n, m))

    print(digit_cancelling_fracs)

    from functools import reduce
    n = reduce((lambda x, t: x * t[0]), digit_cancelling_fracs, 1)
    m = reduce((lambda x, t: x * t[1]), digit_cancelling_fracs, 1)
    print(n, m)
    n, m = simplest_terms(n, m)
    print(n, m)

def fracs_equal(n, m, n2, m2):
    return simplest_terms(n, m) == simplest_terms(n2, m2)

if __name__ == '__main__':
    import sys
    sys.exit(main())
