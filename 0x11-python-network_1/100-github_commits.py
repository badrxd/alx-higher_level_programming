#!/usr/bin/python3
"""script that get the sha and the owner of the commit
"""
import requests
from sys import argv


if __name__ == "__main__":
    """this code will not be executed if it was imported
    """
    url = "https://api.github.com/repos/{}/{}/commits".format(
            argv[1], argv[2])
    r = requests.get(url)
    i = 0
    list_ = r.json()
    for i in range(10):
        owner = list_[i]['commit']['author']['name']
        sha = list_[i]['sha']
        print("{}: {}".format(sha, owner))
