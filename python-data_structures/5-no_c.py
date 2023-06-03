#!/usr/bin/python3
def no_c(my_string):
    string_copy = [char for char in my_string if char != 'C' and char != 'c']
    new_string = ""
    for char in string_copy:
        new_string += char
    return new_string
