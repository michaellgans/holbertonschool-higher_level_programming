#!/usr/bin/python3
""" Defines a class """


class Square:
    """ Names the class Square """
    def __init__(self, size=0):
        """ Initiazlies the data """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Calculates the area of the square """
        area = self.__size * self.__size
        return area
    