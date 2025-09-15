def solution(N, stages):
    answer = []
    total = len(stages)
    rate = {}
    for i in range(1, N + 1):
        if total == 0:
            rate[i] = 0
        else:
            no_clear = stages.count(i)
            rate[i] = no_clear / total
            total -= no_clear
    fail_rate = sorted(rate.items(), key=lambda item: item[1], reverse=True)
    for i in fail_rate:
        answer.append(i[0])

    return answer
