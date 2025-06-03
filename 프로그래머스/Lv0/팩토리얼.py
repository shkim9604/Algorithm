def solution(n):
    answer = 0
    count = 0
    while 1:
        fac = factorial(count)
        if fac > n:
            break
        count += 1
    answer = count - 1
    return answer


def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)
