#!/usr/bin/python3
"" defines the looup(obj). """
def lookup(obj):
    """ returns a list of names that are available in the specified object"""
    return dir(obj)
