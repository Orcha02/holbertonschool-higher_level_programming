#!/usr/bin/python3
""" Class BaseGeometry (based on 6-base_geometry.py). """


class BaseGeometry:
    def area(self):
        """ Function for attributes """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
