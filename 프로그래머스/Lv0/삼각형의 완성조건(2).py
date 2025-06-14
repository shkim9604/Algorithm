def solution(sides):
    answer = 0
    able = []
    a = max(sides)
    b = min(sides)
    for i in range(a-b+1, a+1):
        able.append(i)
    for j in range(a+1,a+b):
        able.append(j)
    print(able)
    answer = len(able)
    return answer
