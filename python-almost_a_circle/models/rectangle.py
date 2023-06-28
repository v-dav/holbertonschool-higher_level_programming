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

        Raise:
            TypeError: if one of the is not an integer
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets or sets the width of the Rectangle.

        Raise:
            TypeError: if the width is not an integer.
            ValueError: if the width is <= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets or sets the height of the Rectangle.

        Raise:
            TypeError: if the height is not an integer.
            ValueError: if the height is <= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets or sets the x of the Rectangle.

        Raise:
            TypeError: if x is not an integer.
            ValueError: if x is <= 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets or sets the y of the Rectangle.

        Raise:
            TypeError: if y is not an integer.
            ValueError: if y is <= 0
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Public method that calculates the area of a rectangle object
        using its width and height.

        Returns: the rectangle area.
        """
        return self.__width * self.__height

    def display(self):
        """
        This function displays a rectangle made of '#' characters with
        a specified height, width, and position.
        """
        for ord in range(self.__y):
            print()
        for i in range(self.__height):
            for abs in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """
        Returns a string representation of a Rectangle object with its id,
        x and y coordinates, width, and height.

        Returns:
            A formatted string that represents the rectangle
        object. The format of the string is
        "[Rectangle] (id) x/y - width/height".
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """A public instance method that updates the attributes of an object
        based on either positional arguments or keyword arguments.
        """
        if args is not None and args != ():
            attributes = ["id", "width", "height", "x", "y"]
            for attr, arg in zip(attributes, args):
                if arg is not None:
                    setattr(self, attr, arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """A public method that returns a formatted
        dictionary representation of a Rectangle
        """
        a_dict = {"x": self.__x, "y": self.__y, "id": self.id,
                  "height": self.__height, "width": self.__width}
        return a_dict
