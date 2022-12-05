#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    string_length = len(sentence)
    if string_length == 0:
        my_tuple = (0, None)
    else:
        my_tuple = (string_length, sentence[0])
    return my_tuple
