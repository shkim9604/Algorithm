def solution(id_pw, db):
    answer = 'fail'
    for Id,pw in db:
        if Id == id_pw[0]:
            if pw == id_pw[1]:
                answer = "login"
            else:
                answer = "wrong pw"
    return answer
