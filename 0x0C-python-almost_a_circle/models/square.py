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
        """ Setter of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update class Square by assigning attributes"""
        if args:  # Checks if exists
            # Iterate list with index condition
            # Index iterates in the enumerated list(args), then it's compared
            for index, element in enumerate(args):
                if index == 0:
                    self.id = element
                elif index == 1:
                    self.size = element
                elif index == 2:
                    self.x = element
                elif index == 3:
                    self.y = element
        else:
            # items->Returns key-value pairs of dictionary, as tuples in a list
            for key, value in kwargs.items():
                # hasattr->Return True if object(.item) has the attributte(key)
                if hasattr(self, key):
                    # setattr->Set attribute(key) value of object(.item)
                    setattr(self, key, value)

     def to_dictionary(self):
        """ Returns the dictionary representation of a Square"""

        dict_repr_2 = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dict_repr_2
