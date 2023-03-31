#!/usr/bin/python3
""" Sends a request to the URL and displays the body of the response
    decoded in uft-8)
"""
from sys import argv
import urllib.request as inquiry
import urllib.parse as parse
import urllib.error as err

if __name__ == "__main__":
    url = argv[1]

    request = inquiry.Request(url)
    try:
        with inquiry.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except err.HTTPError as e:
        print("Error code: {}".format(e.code))
