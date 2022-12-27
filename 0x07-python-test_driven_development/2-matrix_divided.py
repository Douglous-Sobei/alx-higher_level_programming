#!/usr/bin/python3
"""Defination of a matrix division function."""
def matrix_divided(matrix, div):
    """Divide all elements in the matrix.
    Args:
        matrix(list): A list of lists of ints or floats.
        div (int/float): The divisor
    Raises:
        TypeError: if the matrix contains non-numbers.
        TypeError: if the matrix has rows of different sizes.
        TypeError: if div has a non-integer or non-float.
        ZeroDivisionError: if div is equals to 0.
    Returns:
        The new results of the matrix.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix is of the same size
    row_lengths = [len(row) for row in matrix]
    if not all(length == row_lengths[0] for length in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    divided_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return divided_matrix
