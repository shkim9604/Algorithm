def solution(box, n):
    answer = 1
    answer = (box[0] // n) * (box[1] // n) * (box[2] // n)
    return answer
