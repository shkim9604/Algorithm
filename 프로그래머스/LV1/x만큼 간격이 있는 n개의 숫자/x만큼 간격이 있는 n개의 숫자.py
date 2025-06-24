def solution(x, n):
    answer = []
    count = x
    while n != 0:
        answer.append(count)
        count += x
        n -= 1
    return answer
