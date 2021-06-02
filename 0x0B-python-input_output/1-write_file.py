#!/usr/bin/python3
"""Function writes string to a text file, returns number of chars written"""


def write_file(filename="", text=""):
    """ Write file"""
    with open(filename, 'w') as open_file:
        return open_file.write(text)
