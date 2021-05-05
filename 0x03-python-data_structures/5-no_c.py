#!/usr/bin/python3
def no_c(my_string):
    modified_string = ''
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
# Same as (modified_string += char)
        modified_string = modified_string + char
    return modified_string
# + char to continue the string with the other letters
