from collections import Counter

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

# 기존에는 queue로 처리하려 했으나, 오히려 따로 카운팅을 해줘야하는 문제로 푸는 방식 변경
# - 근데 다른 사람 코드를 보니 tuple로 index와 같이 저장해서 사용하는 경우가 있었음. 천재..
# 매번 max를 호출하면 비효율적으로 0이 됐을 때만 기존 값 제거 후 max 호출
# index 와 location이 같아지는 순간 0으로 바꾼 실행된 프로세스의 수를 리턴