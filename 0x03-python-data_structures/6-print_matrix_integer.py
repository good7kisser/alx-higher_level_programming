#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        if len(i) == 0:
            print()
        for z in range(len(i)):
            print("{:d}".format(i[z]),
                    end="\n" if i is len(submatrix) - 1 else " ")
