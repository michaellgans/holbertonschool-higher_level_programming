#!/usr/bin/python3
""" prints a square with the character # """


def print_square(size):
    """
    Args:
        size (int): size of square

    Raises:
        TypeError: if size isn't an integer
        ValueError: if size is less than 0
        TypeError: if size is a float less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print("")
