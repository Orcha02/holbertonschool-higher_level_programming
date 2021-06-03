#!/usr/bin/python3
""" Class Student that defines a student by: (based on 9-student.py) """


class Student:
    """ Create class Student """
    def __init__(self, first_name, last_name, age):
        """ Initialize class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return self.__dict__
        dict = {}
        for attributes in attrs:
            if attributes in self.__dict__:
                dict[attributes] = self.__dict__[attributes]
        return dict
