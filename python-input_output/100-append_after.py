#!/usr/bin/python3
"""A module with a simple function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a new string after a specified search string in a file.

    Args:
        filename (string): The name of the file that you want to modify
        search_string (string): The string that the function will search for
            in the file
        new_string (string): The string that you want to append after the line
        containing the search_string iN the specified file

    Returns: nothing
    """
    with open(filename, 'r', encoding="utf-8") as f:
        lines_as_list = f.readlines()

    for i in range(len(lines_as_list)):
        if search_string in lines_as_list[i]:
            lines_as_list.insert(i + 1, new_string)

    with open(filename, 'w', encoding="utf-8") as f:
        f.writelines(lines_as_list)
