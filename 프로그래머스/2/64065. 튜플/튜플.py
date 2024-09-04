def solution(s):
    dic = {len(se): se for se in [set(split.split(",")) for split in s[2:len(s)-2].split("},{")]}
    
    answer = []
    
    for i in range(1, len(dic) + 1):
        if i == 1:
            answer.append(int(next(iter(dic[i]))))
        else:
            answer.append(int(next(iter(dic[i] - dic[i-1]))))
        
    return answer

# split을 이용해 각 요소들을 분리하고 set으로 변환, 이후 set의 길이를 키, set을 벨류로 갖는 dict 생성
# 차집합을 통해 작은 요소부터 값을 구해 answer에 append