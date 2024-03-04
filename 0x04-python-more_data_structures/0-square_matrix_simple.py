#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix: A 2-dimensional array (list of lists) containing integers.

    Returns:
        A new matrix with the square value of each element of the input matrix.
        The original matrix is not modified.
    """
    # Create a new matrix to store the squared values
    squared_matrix = []

    # Iterate through each row of the matrix
    for row in matrix:
        # Create a new row for the squared matrix
        squared_row = []
        # Iterate through each element in the row and square it
        for element in row:
            squared_row.append(element ** 2)
        # Append the squared row to the squared matrix
        squared_matrix.append(squared_row)

    return squared_matrix
