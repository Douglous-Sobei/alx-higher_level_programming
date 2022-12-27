#!/usr/bin/python3
"""Defines function that multiplies 2 matrices by using the module NumPy"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    # Check if the matrices can be multiplied
    if m_a.shape[1] != m_b.shape[0]:
        raise ValueError("The matrices cannot be multiplied. The number of columns in matrix A must be equal to the number of rows in matrix B.")

    # Multiply the matrices using NumPy's dot function
    result = np.dot(m_a, m_b)

    return result
