#!/usr/bin/python3
def lookup(obj):
    attributes = []
    methods = []

    """ Get a list of all attributes and methods """
    for attr in dir(obj):
        """ Check if the attribute is a method """
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)

    """ Return a list of attributes and methods """
    return attributes + methods
