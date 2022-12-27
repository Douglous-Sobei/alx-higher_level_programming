#!/usr/bin/python3
"""Defines a matrix multiplication function"""

def matrix_mul(m_a, m_b):
    """This function first checks that m_a and m_b are both lists, and then checks that they are both lists of lists.
    It also checks that they are not empty, and that each element is an integer or a float.
    It then checks that each row in the matrices has the same length, and that the number of columns in m_a is equal to the number of rows in m_b, which is a requirement for matrix multiplication.
    If any of these checks fail, the function raises the appropriate exception.
    If all the checks pass, the function initializes an empty result matrix with the appropriate number of rows and columns, and then performs matrix multiplication using a nested loop structure.
    It finally returns the result matrix.
    """
    # Validate m_a and m_b
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(all(isinstance(i, (int, float)) for i in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(i, (int, float)) for i in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize the result matrix
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
