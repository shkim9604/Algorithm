def solution(numbers):
    answer = -100000001
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            a = numbers[i] * numbers[j]
            if a > answer:
                answer = a

    return answer
