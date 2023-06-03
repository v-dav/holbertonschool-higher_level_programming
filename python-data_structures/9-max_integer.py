#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return
    sorted_list = sorted(my_list)
    return sorted_list[len(my_list) - 1]
