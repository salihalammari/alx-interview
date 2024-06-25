#!/usr/bin/python3
"""
create 0-pascal_triangle.py
"""
def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])

        row.append(1)
        triangle.append(row)

    return triangle
