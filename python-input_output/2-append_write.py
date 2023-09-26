#!/usr/bin/python3
""" Project 3, Task 2 """


def append_write(filename="", text=""):
    """
    Args:
        filename - to be created and appended
        text - what to write/append
    Returns:
        length of document written
    """
    with open(filename, "a+", encoding="UTF-8") as file:
        file.write(text)

    return len(text)
