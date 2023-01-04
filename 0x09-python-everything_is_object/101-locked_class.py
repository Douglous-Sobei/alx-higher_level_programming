#!/usr/bin/python3
class LockedClass:
    """You are not allowed to set any attribute other than 'first_name'"""
    __name__ = ['first_name']
