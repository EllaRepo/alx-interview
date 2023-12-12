#!/usr/bin/python3
"""This module define a function that calculates the fewest number of
    operations needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """calculates the fewest number of operations needed to result in
       exactly n H characters in the file
    Args:
        n: a number
    Return:
        An integer
    """
    if n <= 1:
        return 0
    tot, copied, ops = 1, 1, 1

    while 1:
        if tot == n:
            return ops
        tot += copied
        ops += 1
        if n != tot and n % tot == 0:
            copied = tot
            ops += 1
