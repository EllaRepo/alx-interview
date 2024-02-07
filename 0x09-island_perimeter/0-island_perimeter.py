#!/usr/bin/python3
"""Module defines a method that returns the perimeter of the
   island described in grid
"""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid
    Args:
        grid: a list of list of integers
    Returns:
       Returns the perimeter of the island described in grid
    """
    perimeter = 0

    if grid is None or grid == []:
        return perimeter

    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
