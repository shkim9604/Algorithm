def solution(spell, dic):
    answer = 0
    for i in dic:
        i = set(i)
        count = 0
        for j in spell:
            if j in i:
                count += 1
        if count == len(spell):
            answer = 1
            return answer
    answer = 2
    return answer
