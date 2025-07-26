def solution(k, score):
    answer = []
    honor = []
    for i in score:
        honor.append(i)
        if len(honor) > k:
            del honor[honor.index(min(honor))]
            answer.append(min(honor))
        else:
            answer.append(min(honor))
    return answer
