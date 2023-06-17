#!/usr/bin/python3
"""Module containing a function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """A function that multiplies two matrices

    Args:
        m_a (list): first matrix, a list of lists of integers or floats
        m_b (list): secon matrix, a list of lists of integers or floats

    Returns:
        a new matrix, result of the multiplication of two matrices

    Raises:
        TypeError: if one of the args is not a list or not a list of lists
        ValueError: if one of the args is an empty list or contains data
            types other than integers or floats or if matrices can not be
            multiplied
    """

    # All the checks that need to pass before the program execution
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for a in m_a:
        if type(a) is not list:
            raise TypeError("m_a must be a list of lists")
        row_size_a = len(m_a[0])
        if len(a) != row_size_a:
            raise TypeError("each row of m_a must be of the same size")
        for i in range(len(a)):
            if type(a[i]) is not int and type(a[i]) is not float:
                raise TypeError("m_a should contain only integers or floats")

    nb_col_b = 0
    for b in m_b:
        if type(b) is not list:
            raise TypeError("m_b must be a list of lists")
        row_size_b = len(m_b[0])
        if len(b) != row_size_b:
            raise TypeError("each row of m_b must be of the same size")
        for j in range(len(b)):
            if type(b[j]) is not int and type(b[j]) is not float:
                raise TypeError("m_b should contain only integers or floats")
        nb_col_b += 1

    if row_size_a != nb_col_b:
        raise ValueError("m_a and m_b can't be multiplied")

    # The matrix multiplication part
    new_matrix = []
    for i in range(len(m_a)):  # iterate through rows of m_a
        new_matrix.append([])
        for j in range(len(m_b[0])):  # iterate through columns of m_b
            new_matrix[i].append(0)
            for k in range(len(m_b)):  # iterate through rows of m_b
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]

    return new_matrix
