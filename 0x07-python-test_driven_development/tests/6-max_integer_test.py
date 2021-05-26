#!/usr/bin/python3
""" Unittest for max_integer """
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """unittests for the function def max_integer(list=[])"""
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([4, 6, 5]), 6)

    def test_no_params(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_negative_integer(self):
        self.assertEqual(max_integer([4, -5, 6]), 6)
        self.assertEqual(max_integer([-7, -8, -9]), -7)

if __name__ == '__main__':
    unittest.main()
