def solution(n):
    answer = 1
    start = 1
    end = n // 2 + 1
    while start < end:
        hap = 0
        for i in range(start, end + 1):
            hap += i
            if hap == n:
                answer += 1
                start += 1
                break
            elif hap > n:
                start += 1
                break

    return answer
