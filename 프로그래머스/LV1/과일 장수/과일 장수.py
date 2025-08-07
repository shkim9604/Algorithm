def solution(k, m, score):
    answer = 0
    box = []
    score.sort()
    while True:
        if len(score) + len(box) < m:
            break
        apple = score[-1]
        box.append(apple)
        if len(box) == m:
            answer += min(box) * m
            box = []
        score.pop()
    return answer
