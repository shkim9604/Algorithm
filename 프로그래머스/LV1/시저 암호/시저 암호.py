def solution(s, n):
    answer = ''
    big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
    small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z"]
    for i in s:
        if i == " ":
            answer += " "
        elif i in big:
            temp = ord(i)
            temp += n
            if temp > 90:
                temp -= 26
                answer += chr(temp)
            else:
                answer += chr(temp)
        elif i in small:
            temp = ord(i)
            temp += n
            if temp > 122:
                temp -= 26
                answer += chr(temp)
            else:
                answer += chr(temp)
    return answer
