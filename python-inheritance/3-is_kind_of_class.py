#!/usr/bin/python3
""" Returns True if object is an instant of class """


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False
