def solution(s):
    answer = ""
    number = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}
    word = ""
    for i in s:
        if i.isdigit():
            answer += i
        else:
            word += i
            try:
                answer += str(number[word])
                word = ""
            except:
                pass
    return int(answer)
