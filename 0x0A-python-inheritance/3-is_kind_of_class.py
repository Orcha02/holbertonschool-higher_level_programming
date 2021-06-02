#!/usr/bin/python3
"""
Returns True if the object is an instance of a class that
inherited from the specified class, otherwise return False
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
