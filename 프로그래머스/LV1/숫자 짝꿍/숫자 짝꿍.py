def solution(X, Y):
    answer = ''
    numbers = {"9": 0, "8": 0, "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0, "1": 0, "0": 0}
    x_count = list(set(X))
    y_count = list(set(Y))
    xy_count = []
    for i in x_count:
        if i in y_count:
            xy_count.append(i)
    if xy_count == ["0"]:
        return "0"
    for i in xy_count:
        x = X.count(i)
        y = Y.count(i)
        numbers[i] += min(x, y)
    for i in numbers:
        answer += i * (numbers[i])
    if answer == "":
        answer = "-1"
    return answer
