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
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
