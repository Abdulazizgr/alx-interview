#!/usr/bin/python3

""" Module for 0-minoperations"""
def minOperations(n):
    if n < 2:
        return 0
    ops, num = 0, 2
    while num <= n:
        if n % num == 0:
            ops += num
            n /= num
            num -= 1
        num += 1
    return ops

