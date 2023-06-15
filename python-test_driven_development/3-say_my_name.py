#!/usr/bin/python3
"""A module with a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """A function that prints a name of a person

    Args:
        first_name (string): the string representing the first name
            of the person
        last_name (string, optional): the string representing the last
            name of the person. By default: empty string.

    Returns: nothing

    Raises:
        TypeError: if the first ou last name arguments are not strings
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
