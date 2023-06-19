#!/usr/bin/python3
"""A module with a function that checks an object's instance"""


def is_kind_of_class(obj, a_class):
    """A function that checks if the object is an instance of
    the specified class, or if it is an instance of a class
    that inherited from, the specified class

    Args:
        obj (any object): object to check
        a_class (any class): the specified class

    Returns: (bool): True f the object is an instance of
        the specified class, or if it is an instance of a class
        that inherited from, the specified class. Otherwise, False.
    """
    return isinstance(obj, a_class)
