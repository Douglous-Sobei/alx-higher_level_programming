#!/usr/bin/python3
""" post email """
import requests
from sys import argv

if __name__ == "__main__":
    email = {'email': argv[2]}
    r = requests.post(sys.argv[1], data=email)
    print(r.text)
