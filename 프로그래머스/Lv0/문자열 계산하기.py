def solution(my_string):
    answer = 0
    my_string = my_string.split(" ")
    operator = ""
    for i in my_string:
        if i.isdigit() and answer == 0:
            answer += int(i)
        elif i.isdigit() and answer != 0:
            if operator == "+":
                answer += int(i)
            else:
                answer -= int(i)
        else:
            if i == "+":
                operator = "+"
            else:
                operator = "-"
    return answer
