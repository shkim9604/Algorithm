def solution(lottos, win_nums):
    answer = []
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
    if count + lottos.count(0) >= 6:
        answer.append(1)
    elif count + lottos.count(0) == 5:
        answer.append(2)
    elif count + lottos.count(0) == 4:
        answer.append(3)
    elif count + lottos.count(0) == 3:
        answer.append(4)
    elif count + lottos.count(0) == 2:
        answer.append(5)
    else:
        answer.append(6)

    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    else:
        answer.append(6)
    return answer
