#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        [print(*i) for i in matrix]
    else:
        print("")
