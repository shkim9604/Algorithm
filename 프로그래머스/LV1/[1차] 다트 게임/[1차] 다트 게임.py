def solution(dartResult):
    answer = 0
    multiple = {'S': 1, 'D': 2, 'T': 3}
    score = []
    get_score = []
    option = ["*", "#"]
    word = ''
    for i in dartResult:
        if i.isdigit():
            word += i
        else:
            if i.isalpha():
                word += i
                score.append(word)
                word = ''
            elif i in option:
                word += i
                score[-1] += word
                word = ''
    for i in range(len(score)):
        num = ''
        for j in score[i]:
            if j.isdigit():
                num += j
            elif j.isalpha() and num:
                num = int(num)
                num = pow(num, multiple[j])
                print(num)
            elif j in option:
                if j == '*' and i == 0:
                    num *= 2
                elif j == '*' and i >= 1:
                    num *= 2
                    get_score[-1] *= 2
                elif j == '#':
                    num *= -1
        get_score.append(num)

    answer = sum(get_score)

    return answer
