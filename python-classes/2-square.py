#!/usr/bin/python3
"""A module with a simple Square class"""


class Square:
    """A class that defines a square of a given size"""
    def __init__(self, size=0):
        """This is a constructor function that initializes an object with
        a given size.

        Args:
            size (int): represents the size of an object. It is used
                in the initialization of an object's attributes. If the size
                is not an integer or is less than zero, the code raises a
                TypeError or ValueError, respectively. Otherwise, the size
                is stored as a private attribute, defaults to 0 (optional)"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
