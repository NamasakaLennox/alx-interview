#!/usr/bin/python3
"""
Fewest number of operations needed to result in exactly n H characters
"""


def minOperations(n):
    """
    gets the fewest number of operations needed
    """
    available_chars = 1
    pending_chars = n - 1
    copied_chars = 0
    ops = 0

    while (pending_chars > 0):
        if copied_chars and pending_chars % available_chars:
            ops += 1
        else:
            copied_chars = available_chars
            ops = ops + 2
        available_chars += copied_chars
        pending_chars -= copied_chars
    return ops
