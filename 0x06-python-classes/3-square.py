#!/usr/bin/python3
"""class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """Initializes class square"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = self.__size * self.__size
        return area
