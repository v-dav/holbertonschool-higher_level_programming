#!/usr/bin/python3
"""A module with a Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """A Rectangle class that inherits from Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """A constructor method for the Rectangle class

        Args:
            width (int): the width of the Rectangle
            height (int): the height of the Rectangle
            x (int): the x position of the Recangle
            y (int): the y position of the Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets or sets the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Gets or sets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Gets or sets the x of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Gets or sets the y of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
