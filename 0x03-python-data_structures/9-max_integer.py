#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max = my_list[0]
    length = len(my_list)
    for i in range(length):
        if my_list[i] > max:
            max = my_list[i]
    return max
