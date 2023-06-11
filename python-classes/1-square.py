#!/usr/bin/python3
"""A mmodule with a simple Square class"""


class Square:
    """A class that defines a square of a given size"""
    def __init__(self, size):
        """The class __init__ method
        Args:
            size (int): The size of the square"""
        self.__size = size
