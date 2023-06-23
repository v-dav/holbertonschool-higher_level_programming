#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""


import sys

counter = 0
total_size = 0
status_code_list = ["200", "301", "400", "401", "403", "404", "405", "500"]
metrics = {}


def print_stats():
    """
    The function prints the total file size and a count of each status code.
    """
    print("File size: {}".format(total_size))
    for key, value in sorted(metrics.items()):
        print(f"{key}: {value}")


try:
    try:
        for line in sys.stdin:
            counter += 1
            status = line.split()[-2]
            if status in status_code_list:
                total_size += int(line.split()[-1])
                metrics[status] = metrics.get(status, 0) + 1
            if counter % 10 == 0:
                print_stats()
    except Exception:
        pass

except KeyboardInterrupt:
    print_stats()
    raise
