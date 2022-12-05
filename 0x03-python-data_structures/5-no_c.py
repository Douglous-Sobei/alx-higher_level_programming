#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    for character in string_list:
        if character == 'c' or character == 'C':
            string_list.remove(character)
    return ("".join(string_list))
