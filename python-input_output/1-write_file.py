#!/usr/bin/python3
"""A module with a simple function"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8)
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to open and to write to.
            Optional. Defaults to an empty string.

        text (str): The text to write. Optional. Defaults to an empty string.

    Returns: the number of characters written to the file
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
