def solution(a, b, n):
    answer = 0
    rest = 0

    while True:
        if n == 0 and rest < a:
            break
        elif n == 0 and rest >= a:
            n = rest
            rest = 0
        answer += b * (n // a)
        rest += n % a
        n = b * (n // a)

    return answer
