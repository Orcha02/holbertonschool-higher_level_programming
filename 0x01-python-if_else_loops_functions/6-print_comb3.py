#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(10):
        if (num1 < num2):
            print("{0:d}{1:d}, ".format(num1, num2), end="")
