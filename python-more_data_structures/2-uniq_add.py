#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        a = set(my_list)
        res = 0
        for number in a:
            res += number
        return res
