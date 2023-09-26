#!/usr/bin/python3
""" Project 3, Task 3 """


import json

def to_json_string(my_obj):
    """ returns the JSON representation of my_obj """
    json_object = json.dumps(my_obj)

    return json_object