def solution(n, left, right):
    answer = []
    index = left
    while len(answer) < right - left + 1:
        a = index // n
        b = index % n
        answer.append(max(a + 1, b + 1))
        index += 1

    return answer
