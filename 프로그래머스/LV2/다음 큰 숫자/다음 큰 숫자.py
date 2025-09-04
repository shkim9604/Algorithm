def solution(n):
    answer = 0
    for i in range(n + 1, 1000001):
        a = bin(n).count("1")
        b = bin(i).count("1")
        if a == b:
            answer = i
            break
    return answer
