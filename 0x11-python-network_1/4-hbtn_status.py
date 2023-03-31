
#!/usr/bin/python3
""" fetches http://alx-intranet/hbtn.io/status
    using the requests library.
"""
import requests as req

if __name__ == "__main__":
    request = req.get("https://alx-intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
