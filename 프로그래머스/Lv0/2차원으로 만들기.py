def solution(num_list, n):
    answer = []
    count = 0
    array = []
    for i in num_list:
        array.append(i)
        count += 1
        if count == n:
            answer.append(array)
            array = []
            count = 0
    return answer
