#!/usr/bin/python3
"""
Script takes URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')  # POST data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))  # Decoded in utf-8
