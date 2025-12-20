cache = {}

def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)

def minimum_coins(amount, coins):
    if amount in cache:
        return cache[amount]
    
    if amount == 0:
        return 0
    answer = None
    for coin in coins:
        sub_problem = amount - coin
        if sub_problem < 0:
            continue
        minimum = minimum_coins(sub_problem, coins) + 1
        answer = min_ignore_none(answer, minimum)
    cache[amount] = answer
    return answer


def minimum_coins_iterative(amount, coins):
    cache = {}
    cache[0] = 0 # base case: 0 coins needed for amount 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            sub_problem = i - coin
            if sub_problem < 0:
                continue
            
            cache[i] = min_ignore_none(
                cache.get(i),
                cache.get(sub_problem) + 1
            )
        # print(f"min coins needed to form {i} is {cache.get(i)}")
    return cache[amount]

print(minimum_coins_iterative(
    150,
    [5,4,1]
))