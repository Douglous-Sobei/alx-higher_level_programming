#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as req

if __name__ == "__main__":
    with req.urlopen('https://alx-intranet.hbtn.io/status') as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf-8")))
