'''
Climbing stairs, it takes n steps to reach the top. Each time. you can either climb 1 or 2 steps,
in how many distinct ways you can climb to the top?
'''

# def climb_stairs_recursion(n):
    
def climb_stairs(n):
    cache = {}
    cache[0] = 1
    steps = [1, 2]
    
    for i in range(1, n + 1):
        cache[i] = 0
        for step in steps:
            sub_problem = i - step
            if sub_problem < 0:
                continue
            
            cache[i] = cache.get(i) + cache.get(sub_problem)
    
    return cache[n]

print(f"Steps: {climb_stairs(5)}")