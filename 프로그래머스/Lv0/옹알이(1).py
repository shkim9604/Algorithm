def solution(babbling):
    answer = 0
    talking = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in talking:
            i = i.replace(j, ' ')
        i = i.replace(' ', '')
        if len(i) == 0:
            answer += 1
    return answer
