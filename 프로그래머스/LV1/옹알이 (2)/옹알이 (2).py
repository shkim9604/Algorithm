def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        index = 0
        before = ''
        while index < len(can):
            if can[index] == i[:len(can[index])] and before != can[index]:
                i = i.replace(can[index], "", 1)
                before = can[index]
                index = 0
            else:
                index += 1
        if i == '':
            answer += 1

    return answer
