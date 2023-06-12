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
            TypeError: If the size attribute is not a number
            ValueError: If the size attribute is less than zero
        """
        if type(size) is not int and type(size) is not float:
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A method that calculates the area of the square of size 'size'

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Gets or sets the size of the square.

        When setting the size, the value must be an integer greater than
        or equal to 0.

        Raises:
            TypeError: If the value is not a number.
            ValueError: If the value is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        """The `__eq__` method is used to define the behavior of
        the `==` operator for instances of a class.

        Returns: a boolean value that indicates whether the size
        attribute of the current object is equal to the size attribute
        of the other object.
        """
        return self.__size == other.size

    def __gt__(self, other):
        """The `__gt__` method is used to define the behavior of
        the `>` operator for instances of a class.

        Returns: a boolean value that indicates whether the size
        attribute of the current object is greater to the size attribute
        of the other object.
        """
        return self.__size > other.size

    def __lt__(self, other):
        """The `__lt__` method is used to define the behavior of
        the `<` operator for instances of a class.

        Returns: a boolean value that indicates whether the size
        attribute of the current object is inferiour to the size attribute
        of the other object.
        """
        return self.__size < other.size

    def __ge__(self, other):
        """The `__ge__` method is used to define the behavior of
        the `>=` operator for instances of a class.

        Returns: a boolean value that indicates whether the size
        attribute of the current object is greater or equal
        to the size attribute of the other object.
        """
        return self.__size >= other.size

    def __le__(self, other):
        """The `__le__` method is used to define the behavior of
        the `<=` operator for instances of a class.

        Returns: a boolean value that indicates whether the size
        attribute of the current object is inferiour or equal
        to the size attribute of the other object.
        """
        return self.__size <= other.size

    def __ne__(self, other):
        """The `__ne__` method is used to define the behavior of
        the `!=` operator for instances of a class.

        Returns: a boolean value that indicates whether the size
        attribute of the current object is non equal
        to the size attribute of the other object.
        """
        return self.__size != other.size
