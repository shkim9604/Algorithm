def solution(numbers, k):
    answer = 0
    throw = 2 * (k -1) % len(numbers)
    answer = numbers[throw]
    return answer
