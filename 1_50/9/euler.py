#!/usr/bin/python3

def main():
    i = 0
    for a, b, c in pyth_triplets():
        print(str(i) + ':', a, b, c)

        if a + b + c == 1000:
            break

        i += 1

    print(a, b, c, 'product:', a * b * c)

def pyth_triplets():
    '''
    Generates tuples (a,b,c) that are Pythagorean triplets.
    '''
    k = 0
    while True:
        j = 0
        while j < k:
            i = 0
            while i < j:
                if i**2 + j**2 == k**2:
                    yield i, j, k
                i += 1
            j += 1
        k += 1

if __name__ == '__main__':
    main()
