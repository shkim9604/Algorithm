def solution(dots):
    answer = 0
    loc_array = [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2]]
    for i in loc_array:
        a, b, c, d = i
        a = dots[a]
        b = dots[b]
        c = dots[c]
        d = dots[d]
        x1, y1 = a[0], a[1]
        x2, y2 = b[0], b[1]
        x3, y3 = c[0], c[1]
        x4, y4 = d[0], d[1]
        if (y1 - y2) * (x3 - x4) == (y3 - y4) * (x1 - x2):
            answer = 1

    return answer
