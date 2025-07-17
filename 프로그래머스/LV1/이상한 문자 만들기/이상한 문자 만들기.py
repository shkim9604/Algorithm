def solution(s):
    answer = ''
    s = s.split(" ")
    for i in range(len(s)):
        index = 0
        transfer = ""
        for j in s[i]:
            if index % 2 == 0:
                transfer += j.upper()
                index += 1
            else:
                transfer += j.lower()
                index += 1
        s[i] = transfer
    answer = " ".join(s)
    return answer
