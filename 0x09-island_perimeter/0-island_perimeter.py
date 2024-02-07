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

    h = len(grid)
    w = len(grid[0])

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if grid[i][j]:
                if grid[i - 1][j] == 0:
                    perimeter += 2
                if grid[i][j - 1] == 0:
                    perimeter += 2
    return perimeter
