#!/usr/bin/python3
"""A module with a simple function"""


import json


def from_json_string(my_str):
    """A function that returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_obj (str): the string to turn into the Python object

    Returns:
        An object (Python data structure) represented by a JSON string
    """

    return json.loads(my_str)
