#!/usr/bin/python3
""" Function writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """ Save Object to a file """
    with open(filename, 'w') as json_file:
        return json.dump(my_obj, json_file)
