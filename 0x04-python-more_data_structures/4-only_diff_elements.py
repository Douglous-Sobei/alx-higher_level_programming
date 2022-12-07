#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    difference = list(set(set_2).difference(set_1))
    return difference
