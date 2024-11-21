#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    # Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            # Swap element at (i, j) with (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for row in matrix:
        # Reverse the current row
        row.reverse()

