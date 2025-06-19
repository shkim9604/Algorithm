def solution(num, total):
    answer = []
    for i in range(-100,total+1):
        temp = []
        for j in range(i,i+num):
            temp.append(j)
            if len(temp) == num and sum(temp) == total:
                answer = temp
                break
    return answer

