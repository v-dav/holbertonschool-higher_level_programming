#!/usr/bin/python3
"""A module with a simple function"""


def class_to_json(obj):
    """A function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Args:
        obj (obj): is an instance of a Class

    Returns:
        The dictionary description
    """

    return obj.__dict__
