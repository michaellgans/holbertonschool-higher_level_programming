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
            raise ValueError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
