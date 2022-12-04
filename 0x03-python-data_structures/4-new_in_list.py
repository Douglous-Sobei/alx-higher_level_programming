#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_length = len(my_list) - 1
    if (idx < 0 or idx > list_length):
        return (my_list)
    else:
        updated_list = my_list[:]
        updated_list[idx] = element
        return (updated_list)
