def solution(n):
    answer = n // 7
    remain = n % 7
    if remain >= 1:
        answer += 1
    return answer
