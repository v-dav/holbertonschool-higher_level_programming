#!/usr/bin/python3
"""A module with a MyInt class"""


class MyInt(int):
    """A class that inherits from int and that has
    equality and inequality operaors inverted"""

    def __eq__(self, other):
        """
        The method returns the opposite of the result of the
        built-in int.__eq__ function when comparing two objects.

        Args:
            other (obj): the object being compared to the current object

        Returns:
            The opposite of the result of the built-in method `__eq__()`
            of the `int` class when called with `self` and `other`.
            In other words, it is returning `True` if `self` and `other`
            are not equal, and `False` if they are equal.
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """
        The method returns the opposite of the result of the
        built-in int.__ne__ function when comparing two objects.

        Args:
            other (obj): the object being compared to the current object

        Returns:
            The opposite of the result of the built-in method `__ne__()`
            of the `int` class when called with `self` and `other`.
            In other words, it is returning `False` if `self` and `other`
            are not equal, and `True` if they are equal.
        """
        return int.__eq__(self, other)
