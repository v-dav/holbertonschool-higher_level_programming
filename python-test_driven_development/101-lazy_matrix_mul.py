#!/usr/bin/python3
"""Module containing a function that multiplies two matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """A function that multiplies two matrices using NumPy module

    Args:
        m_a (list): first matrix, a list of lists of integers or floats
        m_b (list): secon matrix, a list of lists of integers or floats

    Returns:
        a new matrix, result of the multiplication of two matrices
    """
    return np.dot(m_a, m_b)
