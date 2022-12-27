#!/usr/bin/python3
"""Defination of an integer addition function."""

def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Float arguments are typecasted to ints before the addition is performed.
    Raises:
        TypeError: if either a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    a = int(a)
    b = int(b)
    return a + b
