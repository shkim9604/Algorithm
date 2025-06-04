def solution(s):
    answer = 0
    number = []
    s = s.split(" ")
    for i in s:
        if i == "Z":
            number.pop()
        else:
            number.append(i)

    for i in number:
        answer += int(i)
    return answer
