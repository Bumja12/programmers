from collections import deque

def solution(n):
    answer = 0
    queue = deque()
    for i in range(n+1):
        queue.append(i)
        while sum(queue) > n:
            queue.popleft()
        if sum(queue) == n:
            answer += 1
        
    return answer

# 앞에서부터 순차적으로 더하고 n보다 합이 커지면 pop을 하면서 수를 맞춰나가도록 작성
# 비효율적이라는 생각이 들지만, 특정 법칙이나 알고리즘을 알아야하는 것 같음