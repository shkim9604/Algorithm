def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    index = 0
    for i in range(len(lost)):
        if lost[index] in reserve:
            reserve.remove(lost[index])
            lost.remove(lost[index])
        else:
            index += 1
    index = 0
    for i in range(len(lost)):
        lost_num = lost[index]
        before = lost_num - 1
        after = lost_num + 1
        if before in reserve:
            lost.remove(lost_num)
            reserve.remove(before)
        elif after in reserve:
            lost.remove(lost_num)
            reserve.remove(after)
        else:
            index += 1
    answer = n - len(lost)
    return answer
