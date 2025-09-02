def solution(s):
    answer = ''
    index = 0
    for i in s:
        if i == ' ':
            answer += i
            index = 0
        elif index == 0:
            answer += i.upper()
            index += 1
        else:
            answer += i.lower()

    return answer
