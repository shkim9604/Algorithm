def solution(survey, choices):
    answer = ''
    ch_type = ["RT", "CF", "JM", "AN"]
    type_score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for s,c in zip(survey, choices):
        if c in [1,2,3]:
            type_score[s[0]] += abs(4-c)
        elif c in [5,6,7]:
            type_score[s[1]] += abs(c - 4)
        else:
            continue
    for i in ch_type:
        a = type_score[i[0]]
        b = type_score[i[1]]
        if a > b:
            answer += i[0]
        elif a < b:
            answer += i[1]
        else:
            answer += i[0]
    return answer
