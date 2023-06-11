#!/usr/bin/python3
"""A module with a simple Square class"""


class Square:
    """A class that defines a square of a given size"""
    def __init__(self, size=0):
        """This is a constructor function that initializes an object with
        a given size.

        Args:
            size (int, optional): represents the size of an object.
                Defaults to 0. It is used in the initialization of an object's
                attributes is stored as a private attribute.

        Raises:
            TypeError: If the size attribute is not an integer
            ValueError: If the size attribute is less than zero"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A method that calculates the area of the square of size 'size'

        Returns:
            int: The area of the square"""
        return self.__size ** 2
