#!/usr/bin/python3
"""A module with a simple function"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to open and to write to.
                Optional. Defaults to an empty string.

        text (str): The text to append. Optional. Defaults to an empty string.

    Returns: the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
