def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        count = []
        for j in range(len(arr1[i])):
            count.append(arr1[i][j] + arr2[i][j])
        answer.append(count)
    return answer
