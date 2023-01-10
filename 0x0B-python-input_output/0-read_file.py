#!/usr/bin/python3
"""
A module containing IO functions
"""

def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")