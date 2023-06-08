#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = None
        result = a / b
        return result
    except ZeroDivisionError:
        return result
    finally:
        print("Inside result: {}".format(result))
