#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
