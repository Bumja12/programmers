def solution(progresses, speeds):
    answer = {}
    
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        days = (remain - 1) // speeds[i] + 1
        
        if not answer:
            answer[days] = 1
        else:
            last_day, value = answer.popitem()
            if days <= last_day:
                answer[last_day] = value + 1
            else:
                answer[last_day] = value
                answer[days] = 1
            
    return list(answer.values())

# 남은 개발량과 개발속도를 통해 개발에 걸리는 시간 계산
# dict는 순서가 보장되므로 비어있다면 값을 넣고, 마지막 값을 꺼내어 개발일자가 더 빠르면 +1, 아니면 새로운 키로 등록
# 밸류만 리스트로 반환