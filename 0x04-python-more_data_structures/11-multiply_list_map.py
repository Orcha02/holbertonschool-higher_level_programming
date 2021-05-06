#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda value: value * number, my_list))

# map() function executes a specified function for each item in an iterable
# (lambda argument : expression)->expression is executed and result is returned
