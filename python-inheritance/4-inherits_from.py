#!/usr/bin/python3
"""A module with a special class checking function"""


def inherits_from(obj, a_class):
    """A function that checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj (any object): object to check
        a_class (any class): the specified class

    Returns: (bool) True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class.
    Otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
