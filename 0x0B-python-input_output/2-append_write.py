#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'a') as open_file:
        return open_file.write(text)

# Return is .write instead of .append to return everything with the append
