#!/usr/bin/python3
""" Function that creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """ Create object from a JSON file """
    with open(filename, 'r') as json_file:
        return json.load(json_file)
