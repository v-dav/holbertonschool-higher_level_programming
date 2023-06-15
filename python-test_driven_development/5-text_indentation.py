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

    separators = [".", "?", ":"]
    result = ""
    new_line = True

    for i in text:
        if new_line and i == " ":
            continue
        result += i
        if i in separators:
            result += "\n\n"
            new_line = True
        else:
            new_line = False

    print(result.strip(), end="")
