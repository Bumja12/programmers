def solution(s, arr = []):
    for i in s:
        if arr and arr[-1] == i:
            arr.pop()
        else:
            arr.append(i)

    return 0 if arr else 1

# 1. 앞에서부터 배열에 추가하고, 마지막 값과 현재 값이 같으면 pop, 아니면 append
# 2. 배열이 비어있으면 1, 아니면 0