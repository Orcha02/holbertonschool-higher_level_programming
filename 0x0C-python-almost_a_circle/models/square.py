#!/usr/bin/python3
""" Class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method, initialize a Square
        -> width and height must be assigned to the value of size
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of class."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)  # width or height

    @property
    def size(self):
        """ Getter of size """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
