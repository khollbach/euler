#!/usr/bin/python3

size = 20

def main():
    # size+1 by size+1 matrix, each entry corresponds to a vertex of the grid
    # in the puzzle, and equals the number of paths from that point to the
    # termination point (bottom right of the puzzle grid).
    # The top-left corner of the matrix is the bottom-right corner of the grid
    # in the puzzle, for convenience. You can think of the path starting in the
    # bottom-right corner of the matrix and terminating in the top-left, if you
    # like.
    matrix = [[None for j in range(size+1)] for i in range(size+1)]

    matrix[0][0] = 1

    for ring in range(1, size+1):
        matrix[ring][0] = 1
        matrix[0][ring] = 1
        for i in range(1, ring):
            matrix[i][ring] = matrix[i-1][ring] + matrix[i][ring-1]
        for j in range(1, ring):
            matrix[ring][j] = matrix[ring-1][j] + matrix[ring][j-1]
        matrix[ring][ring] = matrix[ring-1][ring] + matrix[ring][ring-1]

    print(matrix[size][size])

if __name__ == '__main__':
    main()
