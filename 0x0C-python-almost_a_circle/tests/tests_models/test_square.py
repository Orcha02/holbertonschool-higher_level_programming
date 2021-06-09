#!/usr/bin/python3
"""Unittest cases for Square class"""

import unittest
from models.square import Square


class SquareTest(unittest.TestCase):

    def setUp(self):
        self.sq = Square(1, 5, 4)

    def test_size(self):
        """Test size"""

        self.assertEqual(self.sq.size, 1)

    def test_x(self):
        """test x """

        self.assertEqual(self.sq.x, 5)

    def test_y(self):
        """test y """

        self.assertEqual(self.sq.y, 4)

    def test_negative(self):
        """test negative size"""

        with self.assertRaises(ValueError):
            ob = Square(-1)

    def test_sizeSetter(self):
        """Size is not a integer"""

        self.assertRaises(TypeError, Square, "Hello")
