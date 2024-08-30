def solution(n):
    a, b = 0, 1
    for _ in range(2, n+1):
        sum_ab = a + b
        a = b
        b = sum_ab % 1234567
    
    return b

## 1234567 * x + a 간 연산을 했을 때, 결국 몫과 나머지는 연관관계가 없어 나머지끼리만 계속 계산을 해도 나머지는 문제가 생기지 않는다는 걸 알았습니다.