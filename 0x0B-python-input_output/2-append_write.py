#!/usr/bin/python3
"""Function appends string at end of text file, returns num of chars added"""


def append_write(filename="", text=""):
    """ Append file"""
    with open(filename, 'a') as open_file:
        return open_file.write(text)

# Return is .write instead of .append to return everything with the append
