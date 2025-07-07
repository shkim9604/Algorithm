def solution(n):
    answer = ''
    count = 0
    while count != n:
        count += 1
        if count % 2 != 0:
            answer += "수"
        else:
            answer += "박"
    return answer
