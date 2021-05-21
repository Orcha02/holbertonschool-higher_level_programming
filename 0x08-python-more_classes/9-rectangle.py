#!/usr/bin/python3
"""class Rectangle that defines a rectangle by: (based on 7-rectangle.py)"""


class Rectangle:
    """ Public class attribute"""
    number_of_instances = 0
    print_symbol = "#"
    """Initializes class rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        """
        Public class attribute number_of_instances
        ->Incremented during each new instance instantiation
        """
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Initialize rectangle object with width."""
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
        """Initialize rectangle object with height."""
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
        string_result = ((self.__height) *
                         ((self.__width * str(self.print_symbol)) + '\n'))
        return string_result[:-1]

    def __repr__(self):
        """Returns repr representation of a Rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Print message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        """
        Public class attribute number_of_instances
        ->Decremented during each instance deletion
        """
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        if rect_1.area() >= rect_2.area():
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return Rectangle(size, size)
