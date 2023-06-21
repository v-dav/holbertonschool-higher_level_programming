#!/usr/bin/python3
"""A script that adds all arguments to a Python list,
and then save them to a file
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args_list = sys.argv[1:]

try:
    json_list = load_from_json_file("add_item.json")
    for i in range(len(args_list)):
        json_list.append(args_list[i])
    save_to_json_file(json_list, "add_item.json")
except Exception:
    save_to_json_file(args_list, "add_item.json")
