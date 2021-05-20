#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """Initializes class rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Initialise rectangle object with width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width of rectangle and raise errors"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Initialise rectangle object with height."""
        self.__height = height

    @height.setter
    def height(self, value):
        """Height of rectangle and raise errors"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
