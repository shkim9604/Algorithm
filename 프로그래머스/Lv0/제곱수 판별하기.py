def solution(n):
    answer = 0
    for i in range(1, 1001):
        if pow(i, 2) == n:
            answer = 1
            return answer
    answer = 2

    return answer
