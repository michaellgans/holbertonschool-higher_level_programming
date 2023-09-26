#!/usr/bin/python3
""" Project 3, Task 6 """
import json


def load_from_json_file(filename):
    """ Creates an object from a JSON File """
    with open(filename, "r") as file:
        return json.load(file)
