#!/usr/bin/python3
"""A module with a function that checks
an instance of the speciefied class
"""


def is_same_class(obj, a_class):
    """A function that checks if the object is exactly
    an instance of the specified class

    Args:
        obj (object of any type): the object to check
        a_class (class): a class to compare to

    Returns: (bool) True if the object is exactly the instance
        of the class a_class. False, otherwise
    """
    if type(obj) is a_class:
        return True
    else:
        return False
