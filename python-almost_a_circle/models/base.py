#!/usr/bin/python3
"""A module with a simple class"""

import json


class Base:
    """A simple class that the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and
    to avoid duplicating the same code

    Attributes:
        __nb_objects (int): private class attribute number of instances
        without id provided
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is a constructor function that assigns an ID to an object either
        based on a given ID or by incrementing a counter.

        Args:
            id (int): The "id" parameter is an optional argument that can
            be passed to the constructor of an object. If a value is provided
            for "id", it will be assigned to the object's "id" attribute.
            If no value is provided for "id", a new value will be generated
            and assigned to.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A static method that returns the JSON string representation
        of a list of dictionaries.

        Args:
            list_dictionaries (list): a list of dictionaries

        Returns:
            The JSON representation of a list of dictionaries if it's not
            None and not empty. Otherwise returns a string "[]".
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
