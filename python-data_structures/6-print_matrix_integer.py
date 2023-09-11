#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print("")
