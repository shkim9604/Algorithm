def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        s_map = bin(a | b)
        s_map = s_map[2:]
        s_map = s_map.zfill(n)
        trans = ""
        for j in s_map:
            if j == "1":
                trans += "#"
            elif j == "0":
                trans += " "
        answer.append(trans)
    return answer
