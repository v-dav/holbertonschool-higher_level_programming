#!/usr/bin/python3
"""A module with a BaseGeometry class"""


class BaseGeometry():
    """A base geometry class"""

    def area(self):
        """A public instance method that raises an Exception

        Args: nothing

        Returns: nothing

        Raises: Exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public instance method that valides value argument.

        Args:
            name (str): Name attached to the values
            value (int): Value, must be a positive integer

        Returns: nothing

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
