def solution(numlist, n):
    answer = []
    gap = []
    for i in numlist:
        gap.append(abs(n - i))
    gap_index = []
    for i in range(len(numlist)):
        gap_index.append([gap[i], numlist[i]])
    gap = list(set(gap))
    gap.sort()
    gap_index.sort()
    for i in gap:
        temp = []
        for a, b in gap_index:
            if i == a:
                temp.append(b)
        temp.sort(reverse=True)
        for j in temp:
            answer.append(j)

    return answer
