#!/usr/bin/python3
"""locked class"""
class LockedClass:

"""No attribute creation unless attribute = firs_name"""
    __slots__ = ['first_name']

    def __init__(self):
        """Initialize method"""
        pass
