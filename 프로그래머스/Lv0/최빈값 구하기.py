def solution(array):
    answer = 0
    count_array = list(set(array))
    count = {}
    for i in count_array:
        count[i] = array.count(i)
    count_key = list(count.keys())
    count_values = list(count.values())
    max_num = max(count_values)
    if count_values.count(max_num) >= 2:
        return -1
    index = count_values.index(max(count_values))
    answer = count_key[index]
    return answer

