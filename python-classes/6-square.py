#!/usr/bin/python3
"""A module with a Square class"""


class Square:
    """A class that defines a square of a given size at a given position"""
    def __init__(self, size=0, position=(0, 0)):
        """This is a constructor function that initializes an object with
        a given size and a given position.

        Args:
            size (int, optional): represents the size of an object.
                Defaults to 0. It is used in the initialization of an object's
                attributes is stored as a private attribute.
            position (tup, optional): a tuple of 2 positive integers
                representing the tuple position. Defaults to 0. It is used in
                the initialization of an object's
                attributes and is stored as a private attribute.

        Raises:
            TypeError: If the size attribute is not an integer
            ValueError: If the size attribute is less than zero
        """
        self.__size = size
        self.position = position
        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

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
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Gets or sets the position of the object.

        The position must be a tuple of 2 positive integers.

        Raises:
            TypeError: If the position set is not a tuple of 2 positive
            integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """Prints a square made of "#" characters with a size determined by
        the value of the private attribute "__size". If the size is set to 0,
        prints an empty line. Prints as many empty spaces as the first number
        of position
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
