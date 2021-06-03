#!/usr/bin/python3
"""
Function returns dictionary description with simple data structure (list,
dictionary, string, integer, boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """ Dict representation of a class """
    return obj.__dict__

# __dict__-> Shows as dictionary the object
