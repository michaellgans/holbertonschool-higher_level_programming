#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    keys = list(a_dictionary.keys())
    keys.sort()  # sorts keys list
    # creates new dictionary
    sorted_dict = {x: a_dictionary[x] for x in keys}

    for key in sorted_dict:
        print("{}: {}".format(key, sorted_dict[key]))
