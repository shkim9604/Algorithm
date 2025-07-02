def solution(numbers):
    answer = 0
    a = list(range(0,10))
    for i in a:
        if i not in numbers:
            answer += i
    return answer
