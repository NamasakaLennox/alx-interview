#!/usr/bin/python3
"""
A module that gets the perimeter of an island
"""


def island_perimeter(grid):
    """
    Gets the perimeter of an island
    Args:
        grid: a list of lists representing the island
    Return:
        returns the perimeter of the island
    """
    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0

    # iterate through the rows and columns
    # throwing exception means it's the last cell on check side
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                # check if cell top is water or first row
                if grid[i - 1][j] == 0 or i == 0:
                    perimeter += 1

                # check if cell bottom is water or last row
                try:
                    if grid[i + 1][j] == 0:
                        perimeter += 1
                except IndexError:
                    perimeter += 1

                # check if cell left is water
                if grid[i][j - 1] == 0 or j == 0:
                    perimeter += 1

                # check if cell right is water
                try:
                    if grid[i][j + 1] == 0:
                        perimeter += 1
                except IndexError:
                    perimeter += 1

    return (perimeter)


if __name__ == "__main__":
    # test for the function
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
