"""A Python Unit Test for Rectangle class"""

import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """A unittest class to test the Rectangle Class"""

    def test_Rectangle_noId(self):
        """Test object creation without providing an ID"""
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(0, 0)
        self.r4 = Rectangle(-1, -10)

        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r4.y, 0)

    def test_object_withId(self):
        """Test object creation while providing an ID"""
        self.r1 = Rectangle(10, 2, 0, 0, 12)
        self.r2 = Rectangle(2, 10, 5, 4, 6)
        self.r3 = Rectangle(0, 0, 0, 0, 54)
        self.r4 = Rectangle(-1, -10, -2, -3, -6)

        self.assertEqual(self.r1.id, 12)
        self.assertEqual(self.r2.id, 6)
        self.assertEqual(self.r3.id, 54)
        self.assertEqual(self.r4.id, -6)
