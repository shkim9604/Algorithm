def solution(A, B):
    answer = -1
    if A == B:
        return 0
    a = list(A)
    b = list(B)
    count = 0
    for i in range(len(A)):
        last_word = a[-1]
        a.pop()
        a.insert(0, last_word)
        count += 1
        if a == b:
            answer = count
            break
    return answer
