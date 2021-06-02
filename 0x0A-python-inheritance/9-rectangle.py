#!/usr/bin/python3
""" Class BaseGeometry (based on 8-base_geometry.py). """


BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""Class Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""


class Rectangle(BaseGeometry):
    """ Rectangle class inherited from BaseGeometry class"""
    def __init__(self, width, height):
        """Initialize width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of rectangle"""
        area = self.__width * self.__height
        return area

    def __str__(self):
        """
        Returns string representation of a Rectangle (magic method __str__)
        """
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string
