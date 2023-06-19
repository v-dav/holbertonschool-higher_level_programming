#!/usr/bin/python3
"""A simple module with a function that returns the list
of availables attributes and methods of an object
"""


def lookup(obj):
    """a function that returns the list
of availables attributes and methods of an object
"""
    return dir(obj)
