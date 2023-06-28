"""A Python Unit Test for Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
import json


class TestBaseClass(unittest.TestCase):
    """A unittest class to test the Base Class"""

    def test_object_noId(self):
        """Test object creation without providing an ID"""

        self.b1 = Base()
        self.b2 = Base()
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)

    def test_object_withId(self):
        """Test object creation while providing an ID"""

        self.b3 = Base(146)
        self.b4 = Base(0)
        self.b5 = Base(-5)
        self.b6 = Base(1000000)

        self.assertEqual(self.b3.id, 146)
        self.assertEqual(self.b5.id, -5)
        self.assertEqual(self.b6.id, 1000000)

    def test_toJsonString(self):
        """Test the static method to_json_string"""

        self.r1 = Rectangle(10, 7, 2, 8)
        dictionary = self.r1.to_dictionary()

        json_list_of_dict = Base.to_json_string([dictionary])
        revert_from_json = json.loads(json_list_of_dict)

        a_list_of_dict = []
        a_list_of_dict.append(dictionary)

        self.assertEqual(a_list_of_dict, revert_from_json)
