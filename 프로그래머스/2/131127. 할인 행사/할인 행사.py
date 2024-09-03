def solution(want, number, discount):
    dic = {w: i for i, w in enumerate(want)}
    arr = [0] * len(want)
    answer = 0
    
    for i, dis in enumerate(discount):
        first = discount[i - 10]
        
        if dis in dic:
            arr[dic[dis]] += 1
            
        if i > 9 and first in dic:
            arr[dic[first]] -= 1
                
        if number == arr:
            answer += 1
            
    return answer