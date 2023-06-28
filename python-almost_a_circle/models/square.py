#!/usr/bin/python3
"""A module with a Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        This is a constructor method for a class that initializes the size,
        position, and ID of a Square.

        Args:
            size (int): the size of the object being created.
                It is used to set the width and height of the Square

            x (int): The x-coordinate of the top-left corner of the rectangle.
                It specifies the horizontal position of the rectangle on
                the screen. Defaults to 0 (optional)

            y (int): The parameter "y" represents the vertical position of the
                object on a coordinate plane. In this case, it is being passed
                as an argument to the parent class constructor along with the
                size, x position, and id of the object.
                Defaults to 0 (optional)

            id (int): The "id" parameter is an optional identifier for the
                object being created. It can be used to uniquely identify
                the object and differentiate it from other objects of the same
                class. If no "id" is provided, it will default to None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This method allows to print a string representation of a Square object,
        including its id, x and y coordinates, and width.

        Returns: A formatted string
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """
        A property called "size" that returns the value of the "width"
        attribute and sets both the "width" and "height" attributes
        to the given value when the "size" property is set.

        Return: The value of the width attribute.

        Raise:
            TypeError: if the width is not an integer.
            ValueError: if the width is <= 0
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
