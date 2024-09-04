def solution(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        if i+1 > citation:
            return i
    return len(citations)

# h가 인용수라는 점에 꽂혀서 논문의 수(i) 가 아닌 인용수(citation)를 리턴하여 해결하지 못하는 문제가 있었음
# [6, 4, 1, 0] 에서 h는 2가 되는데, citation 을 리턴하면 4를 리턴하게 됨