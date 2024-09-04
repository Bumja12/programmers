def solution(k, dungeons, answer=0):
    if not dungeons: 
        return answer

    max_dungeons = answer

    for i, dungeon in enumerate(dungeons):
        required_fatigue, consume_fatigue = dungeon

        if k >= required_fatigue:
            new_k = k - consume_fatigue
            remaining_dungeons = dungeons[:i] + dungeons[i+1:]
            max_dungeons = max(max_dungeons, solution(new_k, remaining_dungeons, answer + 1))

    return max_dungeons

## filter가 없는게 가독성도 좋고, 오히려 빠른 것 같아서 수정
## 기존 배열방식을 기존 최댓값과 비교해 그때그때 갱신하도록 수정