def solution(n):
    before = [[0, 0], [0, 1]]
    for i in range(2, n+1):
        remains = before[0][1] + before[1][1]
        share = before[0][0] + before[1][0] + remains // 1234567
        remains = remains % 1234567
        before = [before[1], [share, remains]]
    
    return before[1][1]

# 1. 가장 기본적인 방법으로 배열을 쌓아가며 해보았다.
# - 배열의 인덱스가 너무 많다며 에러가 발생했다.
# 2. 배열을 두개만 쓰면서 치환하면서 계산을 했다.
# - 이제 숫자가 너무 커서 문제가 생겼다.
# 3. 몫과 나머지를 나누어서 계산하도록 수정했다.
# - dict 로 했으면 가독성이 훨씬 좋았겠지만, 편의성을 위해 배열로 작성하였다.
# - before [1] 이 before[0] 이 되고, 두개의 합이 before [1] 이 된다.
# - before[0][0] 과 before[1][0] 의 합 => 몫
# - before[0][1] 과 before[1][1] 의 합 => 나머지
# - 나머지가 1234567 보다 커지면 나머지만 남기고, 몫에 1을 더해준다.
# - 마지막에 before[1][1] 즉 나머지만 리턴해주면 끝!