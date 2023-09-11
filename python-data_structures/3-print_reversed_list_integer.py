#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if type(my_list) is list:
        for x in reversed(my_list):
            print("{:d}".format(x))
