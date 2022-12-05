#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    updated_list = []
    length = len(my_list)
    for i in range(length):
        if my_list[i] % 2 == 0:
            updated_list.append(True)
        else:
            updated_list.append(False)
        return updated_list
