""" 
Given a set of coin value coins = {c1,c2, ... ,ck} and a target sum of money 'm',
how many ways can we form the sum 'm' using these coins?
"""

"""
Bottoms up approach
"""
def how_many_ways(amount, coins):
    memo = {}
    memo[0] = 1 # base case: 1 -> There is exactly 1 way to make amount 0: use no coins
    
    for i in range(1, amount + 1):
        memo[i] = 0

        for coin in coins:
            sub_problem = i - coin
            if sub_problem < 0:
                continue
            memo[i] = memo[i] + memo[sub_problem]
    
    return memo[amount]

print(how_many_ways(
    5,
    [5,4,1]
))