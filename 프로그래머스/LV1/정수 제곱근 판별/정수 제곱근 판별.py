def solution(n):
    answer = 0
    a = pow(n, 0.5)
    float_a = str(a)
    if float_a[-1] == "0":
        answer = pow(a+1,2)
    else:
        answer = -1
    return answer
