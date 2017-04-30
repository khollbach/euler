#!/usr/bin/python3

filename = 'names.txt'

def main():
    names = read_namesfile(filename)
    names.sort()

    score_sum = 0
    for i in range(len(names)):
        score_sum += alphabetical_value(names[i]) * (i + 1)

    print(score_sum)

def read_namesfile(filename):
    '''(str) -> [str]
    Reads/parses the names file, returning a list of names.
    '''
    with open(filename) as myfile:
        long_string = myfile.read().strip()

    names = long_string.split(',')
    names = [name.replace('"', '') for name in names]

    return names

def alphabetical_value(string):
    return sum(ord(c) - ord('A') + 1 for c in string)

if __name__ == '__main__':
    main()
