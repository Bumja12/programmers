def helper(x, y):
    while y != 0:
        x, y = y, x % y
    return x
    

def solution(arr):
    answer = 1
    for i in arr:
        answer = answer * i // helper(answer, i)
    return answer