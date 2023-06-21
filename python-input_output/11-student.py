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

    def to_json(self, attrs=None):
        """A public instance method that retrieves a dictionary
        representation of a Student instance.

        Args:
            attrs (list): a list of strings with attribute names. Optional.
            Defaults to None.

        Returns: a dictionary representation of a student instance.
            If attrs is a list of strings, only attribute names contained
            in this list must be retrieved.
        """

        if attrs is None or type(attrs) is not list:
            return self.__dict__

        select_dict = {}
        for attr in attrs:
            if type(attr) is not str:
                return self.__dict__
            else:
                if attr in self.__dict__:
                    select_dict[attr] = self.__dict__[attr]
        return select_dict

    def reload_from_json(self, json):
        """Public method that replaces all attributes of the Student instance.

        Args:
            json (dict): a JSON representation of a Student instance

        Return: nothing
        """

        for k, v in json.items():
            if k in self.__dict__:
                self.__dict__[k] = v
