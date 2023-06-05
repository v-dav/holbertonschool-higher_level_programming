#!/usr/bin/python3
def get_item(item):
    return item[1]


def best_score(a_dictionary):
    if a_dictionary:
        sorted_list = sorted(a_dictionary.items(), key=get_item, reverse=True)
        return sorted_list[0][0]
