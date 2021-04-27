#!/usr/bin/python3
for i in range(0, 100):
    print("{0:02d}, ".format(i), end="")
if i == 99:
    print("{0:02d}".format(i))
# {0:02d} 02 makes reference to the width of the number
# To show a 0 before in numbers < 10
