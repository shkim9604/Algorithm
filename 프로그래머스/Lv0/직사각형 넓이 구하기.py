def solution(dots):
    answer = 0
    x = []
    y = []
    for i in dots:
        x.append(i[0])
        y.append(i[1])
    x_side = abs(max(x) - min(x))
    y_side = abs(max(y) - min(y))
    answer = x_side * y_side
    return answer
