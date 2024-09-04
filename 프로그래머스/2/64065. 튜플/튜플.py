def solution(s):
    sets = [set(map(int, group.split(','))) for group in s[2:-2].split("},{")]

    sets.sort(key=len)
    
    answer = []
    prev_set = set()
    
    for current_set in sets:
        answer.append(next(iter(current_set - prev_set)))
        prev_set = current_set
    
    return answer

## 기존 코드는 sets.sort(key=len) 과정이 필요없었기에 nlogn 만큼 시간이 덜 걸렸지만,
## 해당 코드가 가독성 측면이나 논리 측면에서 더 맘에 들어 남겨놓는다.