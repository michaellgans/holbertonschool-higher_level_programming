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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """ calculates the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a representation of rectangle """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """ inherits from rectangle """
    def __init__(self, size):
        """
        Args:
            size (int): positive, size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Calculates the area of a square """
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
