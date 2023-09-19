#!/usr/bin/python3
""" Divides a matrix by div """


def matrix_divided(matrix, div):
    """
        Args:
            matrix (list of list): ints and floats only

        Raises:
            TypeError: if not a list of list of ints or floats
            TypeError: if each row isn't the same length
            ZeroDivisionError: if div is equal to 0

        Return:
            a new matrix where all elements are divided by
            div and rounded to 2 decimal places
        """
    num_columns = len(matrix[0])

    if not matrix:
        raise SyntaxError("invalid syntax")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")

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
