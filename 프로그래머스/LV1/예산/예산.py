def solution(d, budget):
    answer = 0
    hap = 0
    count = 0
    d.sort()
    for i in d:
        hap += i
        count += 1
        if hap > budget:
            hap -= i
            count -= 1
    answer = count
    return answer
