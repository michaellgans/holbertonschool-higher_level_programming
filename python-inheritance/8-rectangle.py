#!/usr/bin/python3
""" Creates a class """


class BaseGeometry:
    """ Empty Class """
    def area(self):
        """ Area of something """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        name - will always be a string
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry """
    def __init__(self, width, height):
        """
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__height = height
        self.__width = width
