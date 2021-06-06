#!/usr/bin/python3
""" First class Base """


class Base:
    """ Class that manage id attributes """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method initialize a Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
