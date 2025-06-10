def solution(my_str, n):
    answer = []
    count = 0
    string = ""
    for i in my_str:
        count += 1
        string += i
        if count == n:
            answer.append(string)
            count = 0
            string = ""
    if string != "":
        answer.append(string)
    return answer
