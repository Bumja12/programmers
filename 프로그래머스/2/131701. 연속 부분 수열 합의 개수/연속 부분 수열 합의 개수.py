def solution(elements):
    answer = set()
    length = len(elements)
    
    for i in range(length):
        temp = 0
        for j in range(length):
            temp += elements[(i+j) % length]
            answer.add(temp)

    return len(answer)
