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
            self.__width = width

        @width.setter
        def width(self, value):
            """ Setter of width """
            self.__width = width

        @property
        def height(self, value):
            """ Getter of height """
            self.__height = height

        @height.setter
        def height(self, value):
            """ Setter of height """
            self.__height = height

        @property
        def x(self, value):
            """ Getter of x """
            self.__x = x

        @x.setter
        def x(self, value):
            """ Setter of x """
            self.__x = x

        @property
        def y(self, value):
            """ Getter of y """
            self.__y = y

        @y.setter
        def y(self, value):
            """ Setter of y """
            self.__y = y
