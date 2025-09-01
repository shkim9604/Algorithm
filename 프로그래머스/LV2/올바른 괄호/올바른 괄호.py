def solution(s):
    answer = True
    s = s.replace("()","")
    a = s.count("(")
    b = s.count(")")
    if s == '':
        pass
    elif s[0] != "(" or s[-1] != ")":
        answer = False
    elif a != b:
        answer = False
    return answer
