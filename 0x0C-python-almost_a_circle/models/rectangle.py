#!/usr/bin/python3
""" Class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method, initialize a Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self, value):
        """ Getter of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self, value):
        """ Getter of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self, value):
        """ Getter of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter of x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self, value):
        """ Getter of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter of y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Public method that returns the area value of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """Public method prints in stdout the Rectangle with '#' (w * H)"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Return string representation of class."""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
           self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """Update class Rectangle by assigning an argument to each attribute"""
        if args is not 0:
            # Iterate list with index condition
            # Index iterates in the enumerated list(args), the it's compared
            for index, element in enumerate(args):
                if index == 0:
                    self.id = element
                elif index == 1:
                    self.__width = element
                elif index == 2:
                    self.__height = element
                elif index == 3:
                    self.__x = element
                elif index == 4:
                    self.__y = element
