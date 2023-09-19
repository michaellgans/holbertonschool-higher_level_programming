#!/usr/bin/python3
""" Creates a class named Rectangle """


class Rectangle:
    """ Initializes the Data for Rectangle class """

    def __init__(self, width=0, height=0):
        """
            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
