#!/usr/bin/python3
"""matrix multiplication using function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return of the multiplication of two matrices.

    Args:
        m_a (list of lists of ints or floats): first matrix.
        m_b (list of lists of ints or floats): second matrix.
    """

    return (np.matmul(m_a, m_b))
