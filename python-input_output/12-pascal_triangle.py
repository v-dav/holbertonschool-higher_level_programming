#!/usr/bin/python3
"""A module with a simple function"""


def pascal_triangle(n):
    """A function that returns a list of lists of integers representing
    the Pascal’s triangle of n.

    Args:
        n (int): The number

    Returns: The list of list of integers if n is > 0. Empty list otherwise.
    """
    triangle = []
    if n > 0:
        for i in range(n):
            n_list = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    n_list.append(1)
                else:
                    n_list.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(n_list)
    return triangle  # Good job Samir
