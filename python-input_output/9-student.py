#!/usr/bin/python3
""" Project 3, Task 9 """


class Student:
    """ Defines a student """
    def __init__(self, first_name, last_name, age):
        """ student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(obj):
        """ dict description """
        return obj.__dict__
