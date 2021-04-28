#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = ord(i) - 32
        else:
            i = ord(i)
        print("{:c}".format(i), end="")
    print("")
