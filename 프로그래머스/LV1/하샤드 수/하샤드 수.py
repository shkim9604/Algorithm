def solution(x):
    answer = True
    hap = 0
    str_x = str(x)
    for i in str_x:
        if i.isdigit():
            hap += int(i)
    if x % hap == 0:
        pass
    else:
        answer = False
    return answer
