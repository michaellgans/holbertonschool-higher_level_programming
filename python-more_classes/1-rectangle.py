#!/usr/bin/python3
""" Creates a class named Rectangle """


class Rectangle:
    """ Defines the rectangle """
    def __init__(self, width=0, height=0):
        """ Initializes the Data """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >=0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
