#!/usr/bin/python3
class LockedClass:
    def __init__(self):
        self.__dict__['first_name'] = None

    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("You are not allowed to set any attribute other than 'first_name'")
