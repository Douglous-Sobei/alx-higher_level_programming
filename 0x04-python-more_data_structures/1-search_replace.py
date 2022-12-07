#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for element, item in enumerate(my_list):
        if item == search:
            my_list[element] = replace
        print(my_list)
