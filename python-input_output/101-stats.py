#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""


import sys
from collections import Counter


def print_stats():
    """
    The function prints the total file size and a count of each status code.

    Args:
        signal: A signal handler function that can be used to handle signals
            received by the program. Optional. Defaults to None.
        frame: A reference to the current stack frame at the time the
    `print_stats` function is called. Optional. Defaults to None.
    """
    print("File size: {}".format(total_size))
    status_code_dict = Counter(status_code_list)
    for status_code, count in status_code_dict.items():
        print("{}: {}".format(status_code, count))


counter = 0
total_size = 0
status_code_list = []
file_size_list = []

for line in sys.stdin:
    counter += 1
    line_list = line.split()
    status_code_list.append(line_list[-2])
    status_code_list.sort()
    file_size_list.append(line_list[-1])
    status_code_dict = Counter(status_code_list)
    total_size += int(line_list[-1])
    if counter % 10 == 0:
        print_stats()
