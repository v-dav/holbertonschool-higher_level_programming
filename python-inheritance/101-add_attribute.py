#!/usr/bin/python3
"""A module with a simple function"""


def add_attribute(obj, attr_name, attr_value):
    """
    The function adds a new attribute to an object if it is possible.

    Args
        obj (obj): The object to which the attribute needs to be added
        attr_name (str): The name of the attribute that we want to add
        attr_value (obj): The value of the attribute that we want to add

    Returns: nothing

    Raises:
        TypeError: if it's not possible to add a new attribute to the object
    """
    if "__slots__" not in dir(obj) and obj.__class__.__module__ != "builtins":
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("can't add new attribute")
