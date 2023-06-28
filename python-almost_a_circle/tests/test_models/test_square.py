"""A Python Unit Test for Square class"""

import unittest
from models.square import Square
from unittest.mock import patch
import io
import os
import json


class TestSquareClass(unittest.TestCase):
    """A unittest class to test the Square Class"""

    def test_Square_noId(self):
        """Test object creation without providing an ID"""

        self.r1 = Square(10, 2)
        self.r2 = Square(2, 10)

        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.height, 2)

    def test_object_withId(self):
        """Test object creation while providing an ID"""

        self.r1 = Square(10, 0, 0, 12)
        self.r2 = Square(2, 5, 4, 6)
        self.r3 = Square(1, 0, 0, 54)
        self.r4 = Square(3, 0, 0, -6)

        self.assertEqual(self.r1.id, 12)
        self.assertEqual(self.r2.id, 6)
        self.assertEqual(self.r3.id, 54)
        self.assertEqual(self.r4.id, -6)

    def test_raise_errors(self):
        """Test validation of the setter methods"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r1 = Square(10, "Hello")

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r2 = Square(24.67, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r3 = Square(0, 25)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r4 = Square(25, -5)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r6 = Square(10, 10, [1, 2, 3], 3)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r8 = Square(10, 10, -5, 0)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s9 = Square(5)
            self.s9.size = "10"

    def test_SquareArea(self):
        """Test to test the Square area calculation"""

        self.r1 = Square(3, 2)
        self.r2 = Square(2, 10)
        self.r3 = Square(8, 0, 0, 12)

        self.assertEqual(self.r1.area(), 9)
        self.assertEqual(self.r2.area(), 4)
        self.assertEqual(self.r3.area(), 64)

    def test_display(self):
        """Test the exepcted Square display"""

        self.r1 = Square(4, 4, 2, 2)
        self.r2 = Square(2, 2, 1, 1)

        with patch("sys.stdout", new=io.StringIO()) as output:
            self.r1.display()
            exp_output = "\n\n    ####\n    ####\n    ####\n    ####\n"
            self.assertEqual(output.getvalue(), exp_output)

        with patch("sys.stdout", new=io.StringIO()) as output:
            self.r2.display()
            expected_output = "\n  ##\n  ##\n"
            self.assertEqual(output.getvalue(), expected_output)

    def test_str(self):
        """Test the display of the Square representation"""

        self.r1 = Square(4, 2, 1, 12)
        self.r2 = Square(5, 1, 1, 100)

        with patch("sys.stdout", new=io.StringIO()) as output:
            print(self.r1)
            expected_output = "[Square] (12) 2/1 - 4\n"
            self.assertEqual(output.getvalue(), expected_output)

        with patch("sys.stdout", new=io.StringIO()) as output:
            print(self.r2)
            expected_output = "[Square] (100) 1/1 - 5\n"
            self.assertEqual(output.getvalue(), expected_output)

    def test_update(self):
        """Test the update class method of the Square"""

        self.r1 = Square(10, 10, 10, 5)

        self.r1.update(89)
        self.assertEqual(self.r1.id, 89)

        """Test with *args"""
        self.r1.update(89, 3, 4, 5)
        with patch("sys.stdout", new=io.StringIO()) as output:
            print(self.r1)
            expected_output = "[Square] (89) 4/5 - 3\n"
            self.assertEqual(output.getvalue(), expected_output)

        """Test with **kwargs"""
        self.r1.update(size=7, id=100, y=1)
        with patch("sys.stdout", new=io.StringIO()) as output:
            print(self.r1)
            expected_output = "[Square] (100) 4/1 - 7\n"
            self.assertEqual(output.getvalue(), expected_output)

    def test_toDict(self):
        """Test the to_dictionary method of the Square"""

        self.s1 = Square(10, 2, 1, 300)
        s1_dictionary = self.s1.to_dictionary()
        exp_output = {'id': 300, 'x': 2, 'size': 10, 'y': 1}

        self.assertDictEqual(s1_dictionary, exp_output)

        self.s2 = Square(1, 1)
        self.s2.update(**s1_dictionary)

        self.assertEqual(self.s2.to_dictionary(), s1_dictionary)
        self.assertNotEqual(self.s1, self.s2)

    def test_toJsonString(self):
        """Test for the Base method"""

        """Test with None"""
        self.assertEqual("[]", Square.to_json_string(None))

        """Test with empty list"""
        self.assertEqual("[]", Square.to_json_string([]))

    def test_saveToFile(self):
        """Test for the save_to_file class method"""

        self.s1 = Square(10, 7, 2, 8)
        self.s2 = Square(2, 4)

        Square.save_to_file([self.s1, self.s2])

        with open("Square.json", "r", encoding="utf-8") as f:
            content = json.load(f)

        self.assertEqual(content, [self.s1.to_dictionary(),
                                   self.s2.to_dictionary()])

        """Test with None"""
        Square.save_to_file(None)
        with open("Square.json", "r", encoding="utf-8") as f:
            content = json.load(f)
        self.assertEqual(content, [])

        """Test with empty list"""
        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as f:
            content = json.load(f)
        self.assertEqual(content, [])

    def test_fromJSONString(self):
        """Test for the from_JSON_string method"""

        list_input = [{'id': 89, 'size': 10, 'x': 4},
                      {'id': 7, 'size': 1, 'y': 7}]

        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)

        self.assertEqual(list_input, list_output)

        """Test with an empty string"""
        list_input2 = []
        json_list_input2 = Square.to_json_string(list_input2)
        list_output2 = Square.from_json_string(json_list_input2)
        self.assertEqual(list_input2, list_output2)

        """Test with None"""
        self.assertEqual([], Square.from_json_string(None))

    def test_create(self):
        """Test for create class method"""

        self.r1 = Square(3, 5, 1, 400)
        r1_dictionary = self.r1.to_dictionary()
        self.r2 = Square.create(**r1_dictionary)

        with patch("sys.stdout", new=io.StringIO()) as output:
            print(self.r1)
            expected_output = "[Square] (400) 5/1 - 3\n"
            self.assertEqual(output.getvalue(), expected_output)

        with patch("sys.stdout", new=io.StringIO()) as output:
            print(self.r2)
            expected_output = "[Square] (400) 5/1 - 3\n"
            self.assertEqual(output.getvalue(), expected_output)

    def test_loadFromFile(self):
        """Test for the class method loadFromFile"""

        self.s1 = Square(10, 7, 2, 8)
        list_rectangles_input = [self.s1]
        Square.save_to_file(list_rectangles_input)
        list_rectangles_output = Square.load_from_file()

        with patch("sys.stdout", new=io.StringIO()) as output:
            for inst in list_rectangles_output:
                print(inst)
                expected_output = "[Square] (8) 7/2 - 10\n"
                self.assertEqual(output.getvalue(), expected_output)
