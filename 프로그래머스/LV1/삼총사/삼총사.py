def solution(number):
    answer = 0
    for i in range(0, len(number) - 2):
        hap = []
        hap.append(number[i])
        for j in range(i + 1, len(number) - 1):
            hap.append(number[j])
            for k in range(j + 1, len(number)):
                hap.append(number[k])
                if sum(hap) == 0:
                    answer += 1
                    hap.pop()
                else:
                    hap.pop()
            hap.pop()
    return answer
