#!/usr/bin/python3
""" Project 3, Task 4 """

import json


def from_json_string(my_str):
    """ returns an object represented by a json string """
    json_object = json.loads(my_str)

    return json_object
