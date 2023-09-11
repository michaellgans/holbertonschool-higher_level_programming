#!/usr/bin/python3

def no_c(my_string):

    translation = {99: None, 67: None}
    new_string = my_string.translate(translation)
    return new_string
