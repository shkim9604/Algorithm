def solution(n):
    answer = ''
    while True:
        answer += str(n % 3)
        n = n // 3
        if n == 0:
            break

    answer = int(answer, 3)

    return answer
