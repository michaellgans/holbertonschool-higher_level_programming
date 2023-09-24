#!/usr/bin/python3
""" Returns a list of available attributes and methods of an object """


def lookup(obj):
    """ object to search """
    return list(dir(obj))
