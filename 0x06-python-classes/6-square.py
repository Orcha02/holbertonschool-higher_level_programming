#!/usr/bin/python3
"""class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """Initializes class square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        try:
            self.position = position
        except TypeError as err:
            print(err)

    @property
    def position(self):
        """Initialise Square object with position."""
        return self.__position

    @position.setter
    def position(self, value):
        """position of square and raise errors"""
        if type(value) is not tuple:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
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
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("{}{}".format(" " * self.position[0], "#" * self.__size))
