#!/usr/bin/python3
""" Task 1, Project 3 """


def write_file(filename="", text=""):
    """
    Args:
        filename - to be created
        text - what to write in filename

    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)

    return len(text)
