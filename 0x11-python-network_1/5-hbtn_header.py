#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
import requests
from sys import argv


if __name__ == "__main__":
    """this code will not be executed if it was imported
    """
    try:
        r = requests.get(argv[1])
        print(r.headers['X-Request-Id'])
    except Exception as e:
        pass
