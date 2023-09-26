#!/usr/bin/python3
""" Task 7 """


class BaseGeometry:
    """ Superclass for Rectangle and Square """
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
        return True
