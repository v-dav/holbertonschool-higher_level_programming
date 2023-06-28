"""A Python Unit Test for Rectangle class"""

import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io
import os
import json


class TestRectangleClass(unittest.TestCase):
    """A unittest class to test the Rectangle Class"""

    def test_Rectangle_noId(self):
        """Test object creation without providing an ID"""

        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)

        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.height, 10)

    def test_object_withId(self):
        """Test object creation while providing an ID"""

        self.r1 = Rectangle(10, 2, 0, 0, 12)
        self.r2 = Rectangle(2, 10, 5, 4, 6)
        self.r3 = Rectangle(1, 2, 0, 0, 54)
        self.r4 = Rectangle(3, 4, 0, 0, -6)

        self.assertEqual(self.r1.id, 12)
        self.assertEqual(self.r2.id, 6)
        self.assertEqual(self.r3.id, 54)
        self.assertEqual(self.r4.id, -6)

    def test_raise_errors(self):
        """Test validation of all the setter methods"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r1 = Rectangle(10, "Hello")

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r2 = Rectangle(24.67, 10)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r3 = Rectangle(0, 25)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r4 = Rectangle(25, -5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r6 = Rectangle(10, 10, [1, 2, 3], 3)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r7 = Rectangle(10, 10, 10, "Hi")

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r8 = Rectangle(10, 10, -5, 0)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r9 = Rectangle(10, 10, 0, -5)

    def test_RectangleArea(self):
        """Test to test the rectangle area calculation"""

        self.r1 = Rectangle(3, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(self.r1.area(), 6)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 56)

    def test_display(self):
        """Test the exepcted Rectangle display"""

        self.r1 = Rectangle(4, 6, 2, 2)
        self.r2 = Rectangle(2, 2, 1, 1)

        with patch("sys.stdout", new=io.StringIO()) as output:
            self.r1.display()
            exp_output = "\n\n  ####\n  ####\n  ####\n  ####\n  ####\n  ####\n"
            self.assertEqual(output.getvalue(), exp_output)

        with patch("sys.stdout", new=io.StringIO()) as output:
            self.r2.display()
            expected_output = "\n ##\n ##\n"
            self.assertEqual(output.getvalue(), expected_output)

    def test_str(self):
        """Test the display of the Rectangle representation"""

        self.r1 = Rectangle(4, 6, 2, 1, 12)
        self.r2 = Rectangle(5, 5, 1, 1, 100)

        with patch("sys.stdout", new=io.StringIO()) as output:
            print(self.r1)
            expected_output = "[Rectangle] (12) 2/1 - 4/6\n"
            self.assertEqual(output.getvalue(), expected_output)

        with patch("sys.stdout", new=io.StringIO()) as output:
            print(self.r2)
            expected_output = "[Rectangle] (100) 1/1 - 5/5\n"
            self.assertEqual(output.getvalue(), expected_output)

    def test_update(self):
        """Test the update class method of the Rectangle"""

        self.r1 = Rectangle(10, 10, 10, 5)

        self.r1.update(89)
        self.assertEqual(self.r1.id, 89)

        """Test with *args"""
        self.r1.update(89, 2, 3, 4, 5)
        with patch("sys.stdout", new=io.StringIO()) as output:
            print(self.r1)
            expected_output = "[Rectangle] (89) 4/5 - 2/3\n"
            self.assertEqual(output.getvalue(), expected_output)

        """Test with **kwargs"""
        self.r1.update(x=1, height=2, y=3, width=4)
        with patch("sys.stdout", new=io.StringIO()) as output:
            print(self.r1)
            expected_output = "[Rectangle] (89) 1/3 - 4/2\n"
            self.assertEqual(output.getvalue(), expected_output)

    def test_toDict(self):
        """Test the to_dictionary method of the Rectangle"""

        self.r1 = Rectangle(10, 2, 1, 9, 200)
        r1_dictionary = self.r1.to_dictionary()
        exp_output = {'x': 1, 'y': 9, 'id': 200, 'height': 2, 'width': 10}

        self.assertDictEqual(r1_dictionary, exp_output)

        self.r2 = Rectangle(1, 1)
        self.r2.update(**r1_dictionary)

        self.assertEqual(self.r2.to_dictionary(), r1_dictionary)
        self.assertNotEqual(self.r1, self.r2)

    def test_toJsonString(self):
        """Test for the Base method"""

        """Test with None"""
        self.assertEqual("[]", Rectangle.to_json_string(None))

        """Test with empty list"""
        self.assertEqual("[]", Rectangle.to_json_string([]))

    def test_saveToFile(self):
        """Test for the save_to_file class method"""

        """Normal tests"""
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)

        Rectangle.save_to_file([self.r1, self.r2])

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            content = json.load(f)

        self.assertEqual(content, [self.r1.to_dictionary(),
                                   self.r2.to_dictionary()])

        """Test with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            content = json.load(f)
        self.assertEqual(content, [])

        """Test with empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            content = json.load(f)
        self.assertEqual(content, [])

    def test_fromJSONString(self):
        """Test for the from_JSON_string method"""

        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]

        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertEqual(list_input, list_output)

        """Test with an empty string"""
        list_input2 = []
        json_list_input2 = Rectangle.to_json_string(list_input2)
        list_output2 = Rectangle.from_json_string(json_list_input2)
        self.assertEqual(list_input2, list_output2)

        """Test with None"""
        self.assertEqual([], Rectangle.from_json_string(None))

    def test_create(self):
        """Test for create class method"""

        self.r1 = Rectangle(3, 5, 1, 0, 400)
        r1_dictionary = self.r1.to_dictionary()
        self.r2 = Rectangle.create(**r1_dictionary)

        with patch("sys.stdout", new=io.StringIO()) as output:
            print(self.r1)
            expected_output = "[Rectangle] (400) 1/0 - 3/5\n"
            self.assertEqual(output.getvalue(), expected_output)

        with patch("sys.stdout", new=io.StringIO()) as output:
            print(self.r2)
            expected_output = "[Rectangle] (400) 1/0 - 3/5\n"
            self.assertEqual(output.getvalue(), expected_output)

    def test_loadFromFile(self):
        """Test for the class method loadFromFile"""

        self.r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [self.r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        with patch("sys.stdout", new=io.StringIO()) as output:
            for inst in list_rectangles_output:
                print(inst)
                expected_output = "[Rectangle] (11) 2/8 - 10/7\n"
                self.assertEqual(output.getvalue(), expected_output)
