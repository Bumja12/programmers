from collections import Counter

def solution(k, tangerine):
    tan_dic = Counter(tangerine)
    
    s = 0
    for i, value in enumerate(sorted(tan_dic.values(), reverse=True)):
        s += value
        if s >= k:
            return i + 1

# dict 없이는 도저히 해결하는 방법이 떠오르지 않음
# Counter 함수의 힘을 빌려 dict 간단하게 생성
# 밸류를 내림차순으로 정렬하여 더하면서 k와 같거나 커지는 순간 리턴