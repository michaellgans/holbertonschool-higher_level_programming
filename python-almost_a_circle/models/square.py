#!/usr/bin/python3
""" Task 10 """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Creates a new subclass of Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Creates private instances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Overwrites Str """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """ Retrieves width of square """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets width of square """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value
