#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    chechs if a given list of integers represent a valid utf-8 encoding
    """
    # Initialize count of continuation bytes
    num_bytes = 0

    # Iterate over each byte in data
    for byte in data:
        # Initialize mask for checking the most significant bit of byte
        mask = 1 << 7

        # If no continuation bytes are expected
        if not num_bytes:
            # Count the number of most significant bits that are 1
            while byte & mask:
                num_bytes += 1
                mask >>= 1

            # If no most significant bits are 1, continue to next byte
            if not num_bytes:
                continue

            # If only one most significant bit is 1 or more than four most
            #  significant bits are 1, return False
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If the two most significant bits are not '10', return False
            if byte >> 6 != 0b10:
                return False

            # Decrement the count of expected continuation bytes
        num_bytes -= 1

    # If all bytes are processed and no continuation byte is expected,
    #  return True
    return num_bytes == 0
