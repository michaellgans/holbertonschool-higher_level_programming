#!/usr/bin/python3

def number_keys(a_dictionary):
    return (0 if not isinstance(a_dictionary, dict)
    else len(a_dictionary) + sum(number_keys(val) for val in a_dictionary.values()))
    res = number_keys(a_dictionary)
    return res
