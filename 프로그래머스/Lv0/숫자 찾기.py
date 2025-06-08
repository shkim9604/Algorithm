def solution(num, k):
    try:
        answer = list(str(num)).index(str(k))
        answer += 1
    except:
        answer = -1
    return answer
