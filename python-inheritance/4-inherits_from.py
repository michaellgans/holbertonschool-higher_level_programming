#!/usr/bin/python3
""" Returns True if the object is an instance of a class """


def inherits_from(obj, a_class):
    """ Checking for inheritance """
    if isinstance(obj, a_class) and obj.__class__ != a_class:
        return True
    else:
        return False
