#!/usr/bin/python3
"""
Take your Github credentials (username and password) and uses
the Github API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    token = argv[2]
    api = 'https://api.github.com/user'
    response = requests.get(api, auth=(user, token))
    json_dic = response.json()
    print(json_dic.get("id"))
