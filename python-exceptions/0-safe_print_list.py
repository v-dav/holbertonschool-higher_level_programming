#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list:
        try:
            printed = 0
            for i in range(x):
                print("{}".format(my_list[i]), end="")
                printed += 1
            print()
            return printed
        except IndexError:
            print()
            return printed
