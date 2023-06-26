"""A Python Unit Test for Rectangle class"""

import unittest
from models.rectangle import Rectangle


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
