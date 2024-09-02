def solution(n, words):
    used_word = set()
    last_word = words[0][0]

    for i, word in enumerate(words):
        if word not in used_word and last_word[-1] == word[0]:
            used_word.add(word)
            last_word = word
        else:
            return [i % n + 1, i // n + 1]

    return [0, 0]