from collections import OrderedDict

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    answer = 0
    cache = OrderedDict()
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            cache.move_to_end(city)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.popitem(last=False)
            cache[city] = True
            answer += 5
        
    return answer