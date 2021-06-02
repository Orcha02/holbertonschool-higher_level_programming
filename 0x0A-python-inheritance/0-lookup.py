#!/usr/bin/python3
""" Returns the list of available attributes and methods of an object """


def lookup(obj):
    """ Function for attributes """
    return dir(obj)

# dir-> Returns all attributes of the passed object
