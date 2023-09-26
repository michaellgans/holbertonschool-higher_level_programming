#!/usr/bin/python3
""" Task 0 """


def read_file(filename=""):
    """ Reads a file with a with statement """
    with open("my_file_0.txt", encoding="utf-8") as file:
        file_contents = file.read()
        print(file_contents, end="")
