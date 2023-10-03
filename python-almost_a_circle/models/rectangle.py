#!/usr/bin/python3
""" Task 1 """


from models.base import Base


class Rectangle(Base):
    """ Creates a new subclass of Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Creates private instances """
        super().__init__(id)
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    @property
    def width(self):
        """ Retrieves width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width of rectangle """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Retrieves height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height of rectangle """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ Retrieves x of rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x of rectangle """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ Retrieves y of rectangle """
        return self.__y

    @x.setter
    def y(self, value):
        """ Sets y of rectangle """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Returns area of Rectangle """
        return self.__height * self.__width
