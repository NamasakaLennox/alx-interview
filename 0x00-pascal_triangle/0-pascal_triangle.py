#!/usr/bin/python3
"""
defines a pascal triangle given n integers
"""


def pascal_triangle(n):
    """
    function that creates a pascal triangle given n integers
    """
    # if no triangle
    if n <= 0:
        return []

    output = [[1]]

    for row in range(1, n + 1):
        temp = []
        for col in range(row):
            try:
                if (col - 1 < 0 or col > row):
                    raise IndexError
                prev = output[row - 1][col - 1]
                follow = output[row - 1][col]
                temp.append(prev + follow)
            except IndexError:
                temp.append(1)
        output.append(temp)

    return (output[1:])
