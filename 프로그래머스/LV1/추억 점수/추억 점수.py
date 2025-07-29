def solution(name, yearning, photo):
    answer = []
    score = dict()
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    for i in photo:
        count = 0
        for j in i:
            try:
                count += score[j]
            except:
                continue
        answer.append(count)

    return answer
