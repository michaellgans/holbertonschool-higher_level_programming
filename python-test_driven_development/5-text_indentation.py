#!/usr/bin/python3
""" Prints a text with 2 new lines after specific characters """


def text_indentation(text):
    """
    Arguments:
        text (str): text to split up

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    delimiters = ".?:"

    flag = False

    for x in range(len(text)):
        if text[x] in delimiters:
            new_text += text[x]
            flag = True
        elif flag and text[x] == " ":
            continue
        elif flag:
            new_text += "\n\n"
            new_text += text[x]
            flag = False
        else:
            new_text += text[x]
    print(new_text, end="")
    print("")
