def solution(n, words):
    last_word = words[0][0]
    used_word = set()

    for i, word in enumerate(words):
        if word not in used_word and last_word[-1] == word[0]:
            used_word.add(word)
            last_word = word
        else:
            return [i % n + 1, i // n + 1]

    return [0, 0]

# last_word[-1] == word[0] 조건을 만족하기 위해 last_word 를 words[0][0]로 초기화
# 사용한 단어는 set을 사용하여 확인
# 반복문을 빠져나온다면 정상적으로 마무리된 것으로 [0, 0] 리턴