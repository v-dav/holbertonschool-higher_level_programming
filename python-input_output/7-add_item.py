#!/usr/bin/python3
"""A script that adds all arguments to a Python list,
and then save them to a file
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    json_list = load_from_json_file("add_item.json")
    for item in sys.argv[1:]:
        json_list.append(item)
    save_to_json_file(json_list, "add_item.json")
except Exception:
    save_to_json_file(sys.argv[1:], "add_item.json")
