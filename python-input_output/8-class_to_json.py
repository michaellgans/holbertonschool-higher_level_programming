#!/usr/bin/python3
""" Project 3, Task 8 """


def class_to_json(obj):
    """ returns a dictionary description for JSON files """
    return obj.__dict__
