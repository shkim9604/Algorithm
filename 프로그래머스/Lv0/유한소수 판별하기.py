import math


def solution(a, b):
    answer = 0
    c = math.gcd(a, b)
    a = a // c
    b = b // c
    gcd = []
    if a % b == 0:
        answer = 1
    else:
        for i in range(2, b+1):
            if b % i == 0:
                gcd.append(i)
        if gcd == []:
            answer = 2
        else:
            for i in gcd:
                if i not in [2, 5]:
                    if i % 2 == 0 or i % 5 == 0:
                        answer = 1
                    else:
                        answer = 2
                        break
                else:
                    answer = 1

    return answer


a = 1
b = 35
print(solution(a, b))
