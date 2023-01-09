#!/usr/bin/python3
"""Defination of class Mylist which inherits list.
"""

class Mylist(list):
    """Implements the sorted list.
    """
    def print_sorted(self):
        """prints sorted list
        """
        print(sorted(self))
