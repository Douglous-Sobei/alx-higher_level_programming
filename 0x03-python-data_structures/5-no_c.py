#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    for char in string_list:
        if char == 'c' or char == 'C':
            string_list.remove(char)
    return("".join(string_list))
