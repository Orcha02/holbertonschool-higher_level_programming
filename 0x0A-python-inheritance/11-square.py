#!/usr/bin/python3
""" Class BaseGeometry (based on 10-rectangle.py). """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle (9-rectangle.py)"""

    def __init__(self, size):
        """Constructor method for square instantiation with size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string representation"""

        return "[Square] {}/{}".format(self.__size, self.__size)
