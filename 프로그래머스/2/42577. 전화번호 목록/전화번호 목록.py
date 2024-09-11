def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

# 도대체 어떻게 해결하는건지 오랜시간 고민을 했다.
# length 가 100만 하나하나 비교하면 O(n2).. 이건 말이 안된다..
# 문자열을 sort 하면 앞에서부터 비교를 하고 정렬하기 때문에 접두어로 갖는 관계라면 바로 다음에 와야만 한다.
# 그렇게 해결해보았다.

# 테스트 13을 통과하지 못했다. 보통 하나만 실패했다면 예외케이스를 놓친 경우이고, 이 경우는, length 가 1인 경우로 보인다. -> 아니다
# 맨 앞에 온다가 조건인데 단순히 a in b 로 해서 틀린것이다. startswith 로 바꿔주었다.