#!/usr/bin/python3
"""Sends a POST request to the URL passed as argument
    with the email as a parameter also passed as argument,
    displays the body of the repsonse(decoded in utf-8)
"""
from sys import argv
import urllib.request as my_request
import urllib.parse as parse

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    email = parse.urlencode(values).encode("ascii")

    request = my_request.Request(url, email)
    with my_request.urlopen(request) as response:
        page = response.read()
        print(page.decode("utf-8"))
