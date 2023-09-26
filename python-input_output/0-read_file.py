#!/usr/bin/python3
""" Task 0 """


def read_file(filename=""):
    """ Reads a file and prints to standard output """
    with open(filename, encoding="UTF-8") as file:
        bytes_read = file.read()
        print(bytes_read, end="")
