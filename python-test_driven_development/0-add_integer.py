#!/usr/bin/python3
"""Adds two integers or floats together"""

def add_integer(a, b=98):
    """ 
    Args:
        a: int or float
        b: int or float

    Raises: 
        TypeError if either a or be are not int or float

    Return:
        Result of a + b as an integer
    """
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")
    
    return a + b
