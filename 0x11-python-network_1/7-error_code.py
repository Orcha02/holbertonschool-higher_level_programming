#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    status = response.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(response.text)
