def solution(s):
    if len(s) % 2: return 0
    
    answer = []
    pair = { "[": "]", "{": "}", "(": ")" }
    
    for i in range(len(s)):
        temp = s[i:] + s[:i]
        result, stack = True, []
        
        for char in temp:
            if char in pair:
                stack.append(char)
            elif not stack or pair[stack.pop()] != char:
                result = False
                break
        answer.append(result)
        
    return sum(answer)

# 짝을 확인하기 위해 pair 라는 dict를 선언하여 올바를 괄호를 확인
# 닫는 괄호일 때 스택이 비어있거나, 스택의 마지막 요소의 pair와 일치하지 않는 경우 False를 반환
# True = 1, False = 0 이라는 점을 활용하여 배열에 담고 sum을 통해 결과 리턴