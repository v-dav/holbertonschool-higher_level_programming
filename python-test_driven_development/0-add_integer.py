#!/usr/bin/python3
"""A module containing a function that adds 2 integers"""


def add_integer(a, b=98):
    """Add two integers

    Args:
        a (int or float): first number. Casted to integer if float
        b (int or float): second number. Casted to integer if float

    Returns:
        The result of the addition of two numbers, in integer

    Raises:
        TypeError: if a or b are not integers or floats
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
