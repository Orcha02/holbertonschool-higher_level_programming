#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    values = {'q': ""}

    if len(argv) == 2:
        letter = argv[1]
        values['q'] = letter
        response = requests.post(url, data=values)
    else:
        response = requests.post(url, data=values)

    try:
        user = response.json()
        if len(user) < 1:
            print("No result")
        else:
            print("[{}] {}".format(user["id"], user["name"]))
    except ValueError:
        print("Not a valid JSON")
