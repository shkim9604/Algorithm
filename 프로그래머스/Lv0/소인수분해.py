def solution(n):
    answer = []
    number = 2
    while True:
        if n // number == 0 and n % number == 1:
            break
        elif n % number == 0:
            n //= number
            answer.append(number)
        else:
            number += 1
    answer = list(set(answer))
    answer.sort()
    return answer

