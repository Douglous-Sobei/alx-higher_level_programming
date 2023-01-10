#!/usr/bin/python3
"""Handles file input and saves to file"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_item(args):
    try:
        my_list = load_from_json_file("add_item.json")
    except:
        my_list = []
    my_list += args
    save_to_json_file(my_list, "add_item.json")

if __name__ == '__main__':
    add_item(sys.argv[1:])
