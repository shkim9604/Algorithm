def solution(array, commands):
    answer = []
    for i,j,k in commands:
        slice_array = array[i-1:j]
        slice_array.sort()
        answer.append(slice_array[k-1])
    return answer
