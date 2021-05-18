#!/usr/bin/python3
# import dis
import math


class MagicClass:
    """Initializes class MagicClass"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of a square"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of a square"""
        return 2 * math.pi * self.__radius
# dis.dis(MagicClass)
