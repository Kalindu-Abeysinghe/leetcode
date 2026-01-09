

def simulate_cache(requests, cache_size):
    cache = []
    cache_hits = 0
    for request in requests:
        print(f"cache_before: {cache}")
        if request in cache:
            print('cache hit')
            cache_hits += 1
            continue
        if len(cache) == cache_size:
            cache.pop(0)
        cache.append(request)
        print(f"cache_after: {cache}")
        
    print(f'cache_hits: {cache_hits}')
    return cache_hits

def get_minimum_size(requests, k):
    unique_request_count = len(set(requests))
    for i in range(1, unique_request_count):
        cache_hits = simulate_cache(requests, i)
        if cache_hits == k:
            return i
    return -1

print(simulate_cache(
    [
        "item3",
        "item4",
        "item2",
        "item6",
        "item4",
        "item3",
        "item7",
        "item4",
        "item3",
        "item6",
        "item3",
        "item4",
        "item8",
        "item4",
        "item6",
    ],
    3
))