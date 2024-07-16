#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    if not isinstance(matrix, list):
        return
    rows = len(matrix)
    if rows == 0:
        return
    cols = len(matrix[0])
    if not all(isinstance(row, list) and len(row) == cols for row in matrix):
        return
    # Perform matrix rotation
    for layer in range(rows // 2):
        first = layer
        last = rows - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
    return matrix
