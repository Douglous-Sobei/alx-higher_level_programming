#!/usr/bin/python3
def no_c(my_string):
    updated_string = ""
    for c in my_string:
        if c not in 'Cc':
            updated_string += c
    return (updated_string)
