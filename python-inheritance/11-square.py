#!/usr/bin/python3
"""A module with the class square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square"""

    def __init__(self, size):
        """A constructor method that initializes a new square object
        with private instance attribute after validation that the value
        is a positive integer

        Args:
            size (int): the size of the Rectangle

        Returns: nothing
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """The __str__ method in Python represents the class
        object as a customized string

        Returns: a formatted string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
