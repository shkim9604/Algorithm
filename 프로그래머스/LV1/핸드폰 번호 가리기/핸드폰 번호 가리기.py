def solution(phone_number):
    answer = ''
    number = phone_number[-4:]
    answer = answer + "*" * len(phone_number[0:-4]) + number
    return answer
