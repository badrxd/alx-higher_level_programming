#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Args:
        matrix (list): A list of lists of type ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        TypeError: If the matrix contains non-numbers.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix (list) the result of the division.
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
        not all(isinstance(row, list) for row in matrix) or not
        all(isinstance(num, int) or isinstance(num, float)
            for num in [num for raw in matrix for num in raw])):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if (not all(len(row) == len(matrix[0]) for row in matrix)):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    list_1 = []
    for row in matrix:
        list_2 = []
        for num in row:
            round_num = round(num / div, 2)
            list_2.append(round_num)
        list_1.append(list_2)

    return(list_1)
