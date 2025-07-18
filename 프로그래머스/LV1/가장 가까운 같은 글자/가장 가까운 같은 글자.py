def solution(s):
    answer = []
    for i in range(len(s)):
        if i == 0:
            answer.append(-1)
        else:
            word = s[i]
            string = s[:i]
            string = "".join(reversed(string))
            if word in string:
                for j in range(len(string)):
                    if string[j] == word:
                        answer.append(j + 1)
                        break
            else:
                answer.append(-1)

    return answer
