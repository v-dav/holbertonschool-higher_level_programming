#!/usr/bin/python3
"""A module containing a rectangle class"""


class Rectangle:
    """
    A class that defines a rectangle

    Attributes:
        number_of_instances (int): represents the number of instances
            of the class
        print_symbol (str): Used as symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """The class constructor method for instantiation of rectangle object.
        Initializes the instance with width and height and increments the
        number of instances

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        of a rectangle object, made up of print_symbol characters
        depending on its width and height.

        Returns:
            The string representation of the rectangle object
        """
        new_string = ""
        if self.__height == 0 or self.__width == 0:
            return new_string
        for i in range(self.__height):
            for j in range(self.__width):
                new_string += str(self.print_symbol)
            if i != self.__height - 1:
                new_string += "\n"
        return new_string

    def __repr__(self):
        """
        The `__repr__` special method is returning an "official" printable
        string representation of a `Rectangle` object. Decrements the
        number of instances with each deletion.

        Returns:
            A formatted customized string
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ This is a destructor method for "rectangle" class,
        that prints a message when an instance of the class is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This static method function compares the areas of two rectangles
        and returns the rectangle with the larger area.

        Args:
            rect_1 (obj: Rectangle): the first object Rectangle to compare
            rect_2 (obj: Rectangle): the second object Rectangle to compare

        Returns:
            either `rect_1` or `rect_2`, depending on which has a greater area.

        Raises:
            TypeError: if one ofe the arguments is not a Rectangle object
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.area()
        area2 = rect_2.area()

        if area1 >= area2:
            return rect_1
        else:
            return rect_2
