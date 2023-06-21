#!/usr/bin/python3
"""A module with a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class heriting from BaseGeometry"""

    def __init__(self, width, height):
        """A constructor method that initializes a new rectangle object
        with private instance attributes after validation that the values
        are positive integers

        Args:
            width (int): the width of the Rectangle
            height (int): the height of the Rectangle

        Returns: nothing
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """The __str__ method in Python represents the class
        object as a customized string

        Returns: a formatted string
        """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)

    def area(self):
        """A public instance method that coputes
        the rectangle area

        Returns: the rectangle area
        """
        return self.__width * self.__height
