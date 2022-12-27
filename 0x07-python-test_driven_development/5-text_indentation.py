#!/usr/bin/python3
"""Defines a function that prints an idented text"""
def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text(str): Prints text
    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indent = True
    for char in text:
        if char in ".?:":
            print(char)
            print()
            indent = True
        elif indent:
            print(char, end="")
            indent = False
        else:
            print(char, end="")
