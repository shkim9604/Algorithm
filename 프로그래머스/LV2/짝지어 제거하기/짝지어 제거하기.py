def solution(s):
    answer = 0
    word = []
    for i in s:
        if len(word) > 0 and i == word[-1]:
            word.pop()
        else:
            word.append(i)
    if word == []:
        answer = 1
    return answer
