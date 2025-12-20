""" 
Given an NxM grid, how many ways a rabbit can get from top left to bottom right corner
if it only move down or right?
"""

def how_many_ways(n, m):
    memo = {}
    
    # populating base cases
    for i in range(1, n + 1):
        memo[(i, 1)] = 1
    for j in range(1, m + 1):
        memo[(1, j)] = 1
        
    # starting without base case
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            memo[(i, j)] = memo[(i - 1, j)] + memo[i, j - 1]
            
    return memo[(n, m)]


print(how_many_ways(18, 6))