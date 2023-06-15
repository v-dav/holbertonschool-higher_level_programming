#!/usr/bin/python3
"""A module with a function that prints a square"""


def print_square(size):
    """A function that prints a square of a given size

    Args:
        size (int): the size of the square to print. Must be a positive integer

    Returns: nothing

    Raises:
        TypeError: if size is other type than an integer
        ValueError: if size is less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
