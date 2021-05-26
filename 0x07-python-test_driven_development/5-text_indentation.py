#!/usr/bin/python3
"""
Function that prints a text with 2 new lines
after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """ Function that prints a text with 2 new lines """
    delimiters = ['?', '.', ':']
    is_space = False

    if type(text) is not (str):
        raise TypeError("text must be a string")

    for character in text:
        if character is " " and is_space is True:
            continue
        if character in delimiters:
            print("{}".format(character), end="")
            print("\n")
            is_space = True
        else:
            print("{}".format(character), end="")
            is_space = False
