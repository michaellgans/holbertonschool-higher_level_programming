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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Retrieves width of square """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets width of square """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Defines which args are at what position """
        if args:
            attributes = ["id", "__size", "__x", "__y"]

            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
