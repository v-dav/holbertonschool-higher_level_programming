#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in my_list[::-1]:
        if isinstance(i, int):
            print("{:d}".format(i))