#!/usr/bin/python3
"""Unittest cases for Base class"""

import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def setUp(self):
        self.rc = Rectangle(1, 2, 5, 4)

    def test_width(self):
        """Test width"""

        self.assertEqual(self.rc.width, 1)

    def test_heihg(self):
        """Test heigh"""

        self.assertEqual(self.rc.height, 2)

    def test_x(self):
        """test x """

        self.assertEqual(self.rc.x, 5)

    def test_y(self):
        """test y """

        self.assertEqual(self.rc.y, 4)

    def test_widthngative(self):
        """test negative width"""

        with self.assertRaises(ValueError):
            ob = Rectangle(-1, 2)

    def test_NegativeHeigh(self):
        """Test negative heigh"""

        self.assertRaises(ValueError, Rectangle, 2, -1)

    def test_heightSetter(self):
        """Height is not a integer"""

        self.assertRaises(TypeError, Rectangle, 1, "Hello")

    def test_widthSetter(self):
        """width is not a integer"""

        self.assertRaises(TypeError, Rectangle, "Hello", 1)
