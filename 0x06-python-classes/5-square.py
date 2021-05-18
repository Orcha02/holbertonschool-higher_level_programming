#!/usr/bin/python3
"""class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """Initializes class square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Initialise Square object with size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Size of square and raise errors"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of a square"""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Prints in square with the '#' character"""
        if self.__size is 0:
            print()
        else:
            for i in range(self.__size):
                print("{}".format('#' * self.__size))
