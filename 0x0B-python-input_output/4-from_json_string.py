#!/usr/bin/python3
"""
Module that returns an objects.
"""

import json

def from_json_string(my_str):
    return json.loads(my_str)
