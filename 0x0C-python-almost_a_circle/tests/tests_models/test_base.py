#!/usr/bin/python3
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

"""
Test case
"""


class test_base(unittest.TestCase):
    """ test class """
    def test_id_none(self):
        """ None id """
        b1 = Base()
        self.assertEqual(1, b1.id)

    def test_id_zero(self):
        """ id zero """
        b2 = Base(0)
        self.assertEqual(0, b2.id)

    def test_id_string(self):
        """ id is not an integer """
        b3 = Base("base")
        self.assertEqual("base", b3.id)
        self.assertIsInstance(b3, Base)

    def test_id_negative(self):
        """ id is negative number"""
        b4 = Base(-13)
        self.assertEqual(-13, b4.id)

if __name__ == '__main__':
    unittest.main()
