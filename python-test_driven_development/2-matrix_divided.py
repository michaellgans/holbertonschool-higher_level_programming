#!/usr/bin/python3
def matrix_divided(matrix, div):

    num_columns = len(matrix[0])

    if not matrix:
        raise SyntaxError("invalid syntax")

    if not all(len(row) == num_columns for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        result.append(new_row)
    return result
