#!/usr/bin/python3
# 1-my_list.py
"""Defines class MyList which inherits list.
"""


class MyList(list):
    """Implements sorted lst
    """

    def print_sorted(self):
        """Prints sorted lst.
    """
        print(sorted(self))
