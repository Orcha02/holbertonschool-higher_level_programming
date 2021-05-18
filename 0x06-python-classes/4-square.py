#!/usr/bin/python3
"""class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """Initializes class square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = self.__size * self.__size
        return area

# @property-> Defines GETTER (to refer just to field size)
# @size.setter-> Prevents to put bad data
