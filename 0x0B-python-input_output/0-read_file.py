#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Read file"""
    with open(filename, 'r') as open_file:
            print(open_file.read(), end="")

# read() same as-> for line in open_file to read it
