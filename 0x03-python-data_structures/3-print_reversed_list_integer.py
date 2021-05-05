#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Can also be written as-> if my_list is not None:
    if not my_list:
        return (None)
    for i in reversed(my_list):
        print("{:d}".format(i))
# Reversed buil-in will iterate the list in reverse order
