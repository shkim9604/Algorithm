def solution(n):
    answer = 0
    jump = []
    for i in range(0, 2000):
        if i == 0:
            jump.append(1)
        elif i == 1:
            jump.append(2)
        else:
            jump.append(jump[-1] + jump[-2])
        if i == n - 1:
            break
    answer = jump[-1] % 1234567
    return answer
