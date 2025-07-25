def solution(strings, n):
    answer = []
    words = []
    for i in strings:
        words.append(i[n])
    words = list(set(words))
    words.sort()
    for i in words:
        arrange = []
        for j in strings:
            if i == j[n]:
                arrange.append(j)
        if len(arrange) >= 2:
            arrange.sort()
        for k in arrange:
            answer.append(k)
    return answer
