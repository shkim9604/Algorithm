def solution(array, n):
    answer = 0
    array.sort()
    close = []
    for i in array:
        close.append(abs( n - i))
    answer = array[close.index(min(close))]
    return answer
