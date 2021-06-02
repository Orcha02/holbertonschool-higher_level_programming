#!/usr/bin/python3
"""
Returns True if the object is an instance of a class that inherited (directly
or indirectly) from the specified class, otherwise return False.
"""


def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class):
        return True
    return False

# issubclass-> checks if instance obj is a subclass of a_class
# type(obj)-> since first param of issubclass must be a class, and type
#             returns class type of the argument(object) passed as parameter
