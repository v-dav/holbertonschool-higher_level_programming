#!/usr/bin/python3
"""A module with a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """A constructor method that initializes a new rectangle object
        with private instance attributes after validation that the values
        are positive integers

        Args:
            width (int): the width of the Rectangle
            height (int): the height of the Rectangle

        Returns: nothing
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
