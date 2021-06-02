#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """Function Equal"""
    def __ne__(self, other):
        return int.__eq__(self, other)

    """Function no equal"""
    def __eq__(self, other):
        return int.__ne__(self, other)

# __ne__-> !=
# __eq__-> ==
