#!/usr/bin/python3
"""A module with a function that prints an indented text"""


def text_indentation(text):
    """
    A function that prints a text with 2 new lines after each
    of these characters: ., ? and :
    There should be no space at the beginning or at the end of each
    printed line.

    Args:
        text (string): the text to indentate. Must be a string

    Returns: nothing

    Raises:
        TypeError: if the text is not string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    space = True

    while i < len(text):
        if space and text[i] == " ":
            i += 1
            continue
        print("{}".format(text[i]), end="")
        if (text[i] == '.' or text[i] == '?' or text[i] == ':')\
                and i + 1 != len(text):
            print("\n")
            space = True
            i += 1
        else:
            space = False
        i += 1
