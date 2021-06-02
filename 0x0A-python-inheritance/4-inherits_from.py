#!/usr/bin/python3
"""
Returns True if the object is an instance of a class that inherited (directly
or indirectly) from the specified class, otherwise return False.
"""


def inherits_from(obj, a_class):
    """ Function for attributes """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False

# issubclass-> checks if instance obj is a subclass of a_class
# type(obj)-> since first param of issubclass must be a class, and type
#             returns class type of the argument(object) passed as parameter
# [type(obj) is not a_class]-> Checks that type (obj) is not
#                               an instance of class a_class
