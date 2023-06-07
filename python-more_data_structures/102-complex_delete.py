#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = []
    for k, v in a_dictionary.items():
        if a_dictionary[k] == value:
            key_list.append(k)
    for key in key_list:
        del a_dictionary[key]
    return a_dictionary
