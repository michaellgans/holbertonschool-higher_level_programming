#!/usr/bin/python3
""" Write the first class """


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id: integer, no test required
        """
        # This ensures that each object created
        # without specifying an id receives a
        # unique id starting from 1 and
        # incrementing with each new object.
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
