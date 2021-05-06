#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in range(len(matrix)):
        square_matrix.append(list(map(lambda i: i * i, matrix[i])))
    return square_matrix
# map() function executes a specified function for each item in an iterable
#      -> will apply its lambda function to the elements of the argument lists
# lambda function can take any number of arguments
