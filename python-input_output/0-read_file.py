#!/usr/bin/python3
""" reads a file """


def read_file(filename=""):
    with open("my_file_0.txt", "r") as file:
        file_contents = file.read()
        print(file_contents, end="")
