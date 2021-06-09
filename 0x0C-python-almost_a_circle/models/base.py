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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        new_file = "{}.json".format(cls.__name__)
        dictionary = []

        if list_objs is not None:
                for i in list_objs:
                        dictionary.append(cls.to_dictionary(i))
        # as-> Creates an alias
        with open(new_file, "w", encoding="UTF8") as the_list:
            the_list.write(cls.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

        if cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Square":
            dummy = cls(2)
            dummy.update(**dictionary)
            return dummy

        if cls.__name__ == "Rectangle":
            dummy = cls(2, 4)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        new_file = "{}.json".format(cls.__name__)
        instances_list = []

        try:
            with open(new_file, mode="r+", encoding="UTF-8") as f:
                json_items = f.read()
            list_of_dicts = cls.from_json_string(json_items)
            for obj in list_of_dicts:
                instances_list.append(cls.create(**obj))
            return instances_list
        except FileNotFoundError:
            pass
