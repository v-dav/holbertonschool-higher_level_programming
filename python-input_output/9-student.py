#!/usr/bin/python3
"""A module containing a class Student"""


class Student:
    """A simple Student Class.

    Attributes:
        first_name (str): Student first name
        last_name (str): Student last name
        age (int): Student age
    """

    def __init__(self, first_name, last_name, age):
        """A Student initialisation contructor method.

        Args:
            first_name (str): Student first name
            last_name (str): Student last name
            age (int): Student age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A public instance method that retrieves a dictionary
        representation of a Student instance.

        Returns: a dictionary representation of a student instance
        """
        return self.__dict__
