def solution(s):
    answer = []
    count = 0
    zero_count = 0
    while True:
        count += 1
        zero_count += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        if s == "1":
            break
    answer.append(count)
    answer.append(zero_count)
    return answer
