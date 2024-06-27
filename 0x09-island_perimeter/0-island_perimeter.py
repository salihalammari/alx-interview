#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): the grid representing the island

    Returns:
        int: the perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0  # Ensure cols is valid even if grid is empty

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top edge
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom edge
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left edge
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right edge
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
