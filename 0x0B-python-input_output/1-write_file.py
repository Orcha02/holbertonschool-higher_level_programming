#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w') as open_file:
        return open_file.write(text)
