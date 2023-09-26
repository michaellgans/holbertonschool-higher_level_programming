#!/usr/bin/python3
""" Task 0 """


def read_file(filename=""):
    """ Reads a file with a with statement """
    if not isinstance(filename, str):
        raise Exception("filename must be a string")
    with open("my_file_0.txt", encoding="utf-8") as file:
        print(file.read(), end="")
