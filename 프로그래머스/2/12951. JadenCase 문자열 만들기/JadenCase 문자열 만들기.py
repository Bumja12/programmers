def solution(s):
    before, answer = '', ''
    for char in s:
        if char != ' ' and not before or before == ' ':
            answer += char.upper()
        else:
            answer += char.lower()
            
        before = char
            
    return answer