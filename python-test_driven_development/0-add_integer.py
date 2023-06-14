#!/usr/bin/python3
"""A module containing a function that adds 2 integers"""


def add_integer(a, b=98):
    """Add two integers

    Args:
        a (int or float): first number. Casted to integer if float
        b (int or float): second number. Casted to integer if float.
        Optional, by default at 98

    Returns:
        The result of the addition of two numbers, in integer

    Raises:
        TypeError: if a or b are not integers or floats
    """
    try:
        return int(a + b)
    except Exception:   
        if type(a) is not int:
            raise TypeError("a must be an integer")
        else:
            raise TypeError("b must be an integer")
