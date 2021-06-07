#!/usr/bin/python3
""" First class Base """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
