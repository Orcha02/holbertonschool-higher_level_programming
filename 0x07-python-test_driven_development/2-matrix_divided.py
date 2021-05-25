#!/usr/bin/python3
""" Function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    Matrix must be a list of lists
    of integers, floats.
    Return: a new matrix
    """

    m_error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list and type(matrix) not in (int, float):
        raise TypeError(m_error)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(m_error)
        for column in row:
            if type(column) not in (int, float):
                raise TypeError(m_error)
    if len(matrix[0]) is not len(row):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = [[round(element / div, 2) for element in row]
                      for row in matrix]
    return(new_matrix)
