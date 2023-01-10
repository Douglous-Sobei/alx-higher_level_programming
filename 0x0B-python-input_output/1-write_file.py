#!/usr/bin/python3
"""defines the file to be written"""

def write_file(filename="", text=""):
    """writes a string to a text file (UTF8).
    returns the number of characters written.
    """
    with open(filename, "w", encoding="utf8") as file:
        file.write(text)
        return len(text)
