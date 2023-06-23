#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""


import sys
from collections import Counter

counter = 0
total_size = 0
status_code_list = []
file_size_list = []


def print_stats():
    """
    The function prints the total file size and a count of each status code.
    """
    print("File size: {}".format(total_size))
    status_code_dict = Counter(status_code_list)
    for status_code, count in status_code_dict.items():
        print("{}: {}".format(status_code, count))


try:
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

except KeyboardInterrupt:
    print_stats()
    raise
