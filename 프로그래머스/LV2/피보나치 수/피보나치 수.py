def solution(n):
    answer = 0
    before = 0
    current = 1

    for i in range(2, n + 1):
        answer = before + current
        temp = before
        before = current
        current = current + temp

    answer = answer % 1234567

    return answer
