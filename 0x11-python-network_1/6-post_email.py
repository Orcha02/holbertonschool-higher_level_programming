#!/usr/bin/python3
"""
Takes in a URL and email, sends a POST request to the passed URL
with the email as a parameter, and finally
displays the body of the response."""
import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    mail_ar = argv[2]
    values = {'email': mail_ar}
    response = requests.post(url, data=values)
    print(response.text)
