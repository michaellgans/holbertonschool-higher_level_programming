#!/usr/bin/python3
""" Project 3, last one """


def pascal_triangle(n):
    """ returns a list of list of ints representing Pascal's triangle """
    if n <= 0:
        return []

    chameleon = [[1]]
    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            row.append(chameleon[x - 1][y - 1] + chameleon[x - 1][y])
        row.append(1)
        chameleon.append(row)

    return chameleon
