def solution(hp):
    answer = 0
    general = 5
    captain = 3
    normal = 1
    answer += hp // general
    hp %= general
    answer += hp // captain
    hp %= captain
    if hp == 0:
        return answer
    else:
        answer += hp // normal
    return answer
