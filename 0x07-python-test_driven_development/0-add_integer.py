#!/usr/bin/python3
"""
0-add_integer: Must add 2 ints
a and b must be integers or float, otherwise raise TypeError
float must be converted to int
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers.
    Returns: Add a, b"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a + b)
