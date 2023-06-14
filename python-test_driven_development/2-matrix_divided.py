#!/usr/bin/python3
"""Module containing a function for dividing elements of a matrix"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix."""

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        first_row_length = len(matrix[0])

        if len(i) != first_row_length:
            raise TypeError("Each row of the matrix "
                            "must have the same size")

        a_list = []
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            a_list.append(round(j / div, 2))
        new_matrix.append(a_list)
    return new_matrix
