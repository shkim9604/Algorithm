def solution(n):
    answer = 0
    for i in range(n, n * 6 + 1):
        if i % 6 == 0 and i % n == 0:
            answer = i
            break
    answer = answer // 6
    return answer
