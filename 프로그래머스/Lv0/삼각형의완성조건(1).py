def solution(sides):
    answer = 0
    big_num = max(sides)
    sides.remove(big_num)
    if big_num < sum(sides):
        answer = 1
    else:
        answer = 2
    return answer
