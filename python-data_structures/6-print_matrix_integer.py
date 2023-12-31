#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    columns = len(matrix[0])
    if not matrix:
        columns = 0
    for row in matrix:
        for x, element in enumerate(row):
            if x == columns - 1:
                print("{:d}".format(element), end="")
            else:
                print("{:d}".format(element), end=" ")
        print()
