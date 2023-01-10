#!/usr/bin/python3
"""
Module for write_file method.
"""


def write_file(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and returns the number of characters added:"""
    with open(filename, mode="w", encoding="UTF-8") as f:
        return (f.write(text))
