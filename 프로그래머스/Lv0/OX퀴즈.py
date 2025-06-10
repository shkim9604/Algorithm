def solution(quiz):
    answer = []
    for i in quiz:
        i = i.split("=")
        result = int(i[-1])
        equation = i[0].split()
        a, operator, b = equation
        if operator == "+":
            num = int(a) + int(b)
        else:
            num = int(a) - int(b)
        if result == num:
            answer.append("O")
        else:
            answer.append("X")
    return answer


