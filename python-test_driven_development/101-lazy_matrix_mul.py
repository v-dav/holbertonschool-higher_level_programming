#!/usr/bin/python3
"""Module containing a function that multiplies two matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    return np.matmul(m_a, m_b)
