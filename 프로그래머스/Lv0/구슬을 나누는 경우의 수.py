def solution(balls, share):
    answer = 0
    up = 1
    down = 1
    for i in range(1,balls+1):
        up *= i
    for i in range(1, balls+1-share):
        down *= i
    for i in range(1, share+1):
        down *= i
    answer = up // down
    return answer

