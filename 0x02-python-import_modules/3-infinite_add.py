#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    output = 0
    for i in argv[1:]:
        # += To add them and not just show last one
        output += int(i)
    print(output)
# argv-> List containing the arguments passed
# [1:]-> Count arguments by (1) to undefined (: )
