#!/usr/bin/python3
"""
    function to add two int
"""


def add_integer(a, b=98):
    """ function to add two integers """
    try:
        result = a + b
        return int(result)
    except:
        if type(a) is not int:
            raise TypeError("a must be an integer")
        else:
            raise TypeError("b must be an integer")
