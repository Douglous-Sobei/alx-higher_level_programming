#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        my_result = a / b
    except ZeroDivisionError:
        my_result = None
    finally:
        print("Inside result: {}".format(my_result))
    return my_result
