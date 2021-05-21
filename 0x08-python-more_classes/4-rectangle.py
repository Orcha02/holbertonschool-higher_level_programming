#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 3-rectangle.py)"""


class Rectangle:
    """Initializes class rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
        return self.__height

    @height.setter
    def height(self, value):
        """Height of rectangle and raise errors"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns string representation of a Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        string_result = ((self.__height) * ((self.__width * '#') + '\n'))
        return string_result[:-1]

    def __repr__(self):
        """Returns repr representation of a Rectangle"""
        return ("Rectangle({},{})".format(self.__width, self.__height))
