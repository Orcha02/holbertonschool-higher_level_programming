#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as open_file:
            print(open_file.read(), end="")

# read() same as-> for line in open_file to read it
