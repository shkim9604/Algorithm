def solution(s):
    answer = ''
    s = s.split(" ")
    trans = []
    for i in s:
        trans.append(int(i))
    answer += str(min(trans)) + " " + str(max(trans))
    return answer