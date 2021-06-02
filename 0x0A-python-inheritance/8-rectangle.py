#!/usr/bin/python3
""" Class BaseGeometry (based on 7-base_geometry.py). """


class BaseGeometry:
    """ BaseGeometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

# Could just put instead of all the code above:
# BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""Class Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

# Missed the TypeError in output so added super()
# super()-> Gives access to methods and properties of its parent
