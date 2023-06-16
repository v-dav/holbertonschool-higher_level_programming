#!/usr/bin/python3
"""A module containing a rectangle class"""


class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """The class constructor method for instantiation of rectangle object.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets or sets the width of the rectangle.

        When setting the width the value must be an integer equal or superiour
        to zero.

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets or sets the height of the rectangle.

        When setting the height the value must be an integer equal or superiour
        to zero.

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A public method that retrieves the rectangle's area

        Returns: the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """A public method that retrieves the rectangle's perimeter

        Returns: the perimeter of the rectangle. 0 if width or height is 0.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """
        The `__str__` special method is returning a string representation
        of a rectangle object, made up of "#" characters depending on its
        width and height.

        Returns:
            The string representation of the rectangle object
        """
        new_string = ""
        if self.__height == 0 or self.__width == 0:
            return new_string
        for i in range(self.__height):
            for j in range(self.__width):
                new_string += "#"
            if i != self.__height - 1:
                new_string += "\n"
        return new_string

    def __repr__(self):
        """
        The `__repr__` special method is returning an "official" printable
        string representation of a `Rectangle` object.

        Returns:
            A formatted customized string
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ This is a destructor method for "rectangle" class,
        that prints a message when an instance of the class is deleted.
        """
        print("Bye rectangle...")
