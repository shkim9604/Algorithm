def solution(s):
    answer = True
    s = s.lower()
    p = s.count("p")
    y = s.count("y")
    if p == y:
        return answer
    else:
        answer = False

    return answer
