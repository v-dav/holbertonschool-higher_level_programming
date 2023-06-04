#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    sorted_dictionary = {i: a_dictionary[i] for i in keys}
    for key in sorted_dictionary:
        print("{}: {}".format(key, sorted_dictionary[key]))
