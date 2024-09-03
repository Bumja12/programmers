from collections import Counter
from functools import reduce

def solution(clothes):
    clothes_dict = Counter([c[1] for c in clothes])
    
    answer = reduce(lambda x, y: x * (y + 1), clothes_dict.values(), 1)
    return answer - 1
