#!/usr/bin/python3
"""Definition of a function that prints name."""
def say_my_name(first_name, last_name=""):
    """Prints name.
    Args:
        first_name(str): First name to be printed
        last_name(str): Last name to be printed
    Raises:
        TypeError: if either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name and last_name must be strings")
    print("My name is {} {}".format(first_name, last_name))

