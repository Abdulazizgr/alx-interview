#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, num = 0, 2
    while num <= n:
        # if n evenly divides by num
        if n % num == 0:
            # total even-divisions by num = total operations
            ops += num
            
            n = n / num
            
            num -= 1
        
        num += 1
    return ops
