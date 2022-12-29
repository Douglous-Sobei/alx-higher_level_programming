#!/usr/bin/python3
"""Defines a function which prints a square"""

def print_square(size):
    """Prints a Square wit an # character.
    Args:
        size(int): The height/width of the square.
    Raises:
        TypeError: if the size is a non-integer
        ValueError: if the value is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
