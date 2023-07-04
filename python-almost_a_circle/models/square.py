#!/usr/bin/python3
"""Module defining the Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the attributes and methods of the Square class that inherits
    from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method for the Square class.

        Args:
            size (int): Determines the size of a Square instance
            x (int): Position of the square on the x axis
            y (int): Position of the square on the y axis
            id (int): id of the Square instance
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute of a Square instance"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute of a Square instance

        Args:
            value (int): Positive integer. Defines the size of a square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to zero
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """Defines the string representation of a Square object"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """Allows the user to update a square's attributes after it was
        created."""

        if args:
            position = 1
            for arg in args:
                if position == 1:
                    self.id = arg
                elif position == 2:
                    self.width = arg
                    self.height = arg
                elif position == 3:
                    self.x = arg
                elif position == 4:
                    self.y = arg

                position += 1

        else:
            for attr, value in kwargs.items():
                if attr == "size":
                    self.width = value
                    self.height = value
                elif attr == "x":
                    self.x = value
                elif attr == "y":
                    self.y = value
                elif attr == "id":
                    self.id = value

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""

        my_dict = {}
        for attr, value in self.__dict__.items():
            if attr == "id":
                my_dict["id"] = value
            elif attr == "_Rectangle__width":
                my_dict["size"] = value
            elif attr == "_Rectangle__x":
                my_dict["x"] = value
            elif attr == "_Rectangle__y":
                my_dict["y"] = value
        return my_dict
