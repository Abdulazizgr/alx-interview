#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows for Pascal's triangle.

    Returns:
        list: A list of lists, representing Pascal's triangle.
    """
    if n <= 0:
        return []
    
    dp = [[1]]  

    for i in range(1, n):
        curr = [1]  
        for j in range(1, len(dp[-1])):
           
            curr.append(dp[-1][j - 1] + dp[-1][j])
        curr.append(1)  
        dp.append(curr)

    return dp
