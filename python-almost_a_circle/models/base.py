#!/usr/bin/python3
"""Module defining the Base class"""


import json
from os.path import exists


class Base:
    """Defines the attributes and methods of the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method for the Base class.

        Args:
            id (int): Positive integer to set class instance's id to.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of 'list_dictionaries'"""

        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of 'list_objs' to a file"""
        if not list_objs:
            list_objs = []

        my_list = []
        for obj in list_objs:
            my_list.append(obj.to_dictionary())

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            f.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON representation 'json_string'"""

        if not json_string or json_string == []:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes already set"""

        dummy = cls(3, 5)
        dummy.x = 0
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file containing JSON string
        representation of a class 'cls' object"""

        filename = "{}.json".format(cls.__name__)
        if not exists(filename):
            return []

        with open(filename, "r") as f:
            json_str = f.read()
            json_list = cls.from_json_string(json_str)
            list_objs = []
            for dict in json_list:
                list_objs.append(cls.create(**dict))

            return list_objs
