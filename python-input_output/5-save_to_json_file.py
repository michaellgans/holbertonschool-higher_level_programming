#!/usr/bin/python3
""" Project 3, Task 5 """

import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a txt file """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
