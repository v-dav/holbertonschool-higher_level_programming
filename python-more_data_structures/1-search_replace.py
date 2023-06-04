#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(my_list[i])
    idx = my_list.index(search)
    new_list[idx] = replace
    return new_list
