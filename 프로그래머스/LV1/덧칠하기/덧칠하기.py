def solution(n, m, section):
    answer = 0
    paint_pos = 0
    for i in section:
        if i > paint_pos:
            answer += 1
            paint_pos = i + m - 1
    return answer
