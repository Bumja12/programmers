def solution(k, dungeons, answer = 1):
    if not dungeons: 
        return answer - 1

    arr = []
    for dungeon in dungeons:
        current_fatigue = k - dungeon[1]

        i = dungeons.index(dungeon)
        new_dungeons = list(filter(lambda x: x[0] <= current_fatigue, dungeons[:i] + dungeons[i+1:]))
        arr.append(solution(current_fatigue, new_dungeons, answer + 1))

    return max(arr)

# 단순 정렬만으로는 답이 나올 수 없어 보임
# 결국 순회를 해야하는데, 어차피 길이가 8인 배열이므로 그냥 순회하기로 결정
# 그래도 최소한의 순회를 하기 위해 filter 를 이용해 갈 수 있는 던전만 입력
# 갈 수 있는 모든 던전을 도는 경우의 수를 list에 담고 최댓값을 리턴