#!/usr/bin/python3
""" Returns True if object is an instant of class """


def is_kind_of_class(obj, a_class):
    """ obj - object to check.  a_class - class to check """
    if isinstance(obj, a_class):
        return True
    else:
        return False
