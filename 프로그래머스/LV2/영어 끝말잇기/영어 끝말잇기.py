def solution(n, words):
    answer = []
    before_talk = [words[0]]
    for i in range(1,len(words)):
        if words[i] in before_talk:
            answer.append(i % n + 1)
            answer.append(i // n  + 1)
            break
        if before_talk[-1][-1] == words[i][0]:
            before_talk.append(words[i])
        else:
            answer.append(i % n + 1)
            answer.append(i // n  + 1)
            break
    if answer == []:
        answer = [0, 0]
    return answer
