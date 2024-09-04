from collections import Counter, deque

def solution(priorities, location):
    counter = Counter(priorities)
    maxx = max(counter.keys())
    
    while True:
        for i, p in enumerate(priorities):
            if maxx == p:
                counter[p] -= 1
                priorities[i] = 0
                
                if i == location:
                    return priorities.count(0)
                
                if counter[p] == 0:
                    del counter[maxx]
                    maxx = max(counter.keys())
