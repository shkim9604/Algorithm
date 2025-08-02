def solution(s, skip, index):
    answer = ''
    skip = list(skip)
    for i in s:
        count = 0
        word_num = ord(i)
        while True:
            word_num += 1
            count += 1
            if word_num > 122:
                word_num -= 26
            if chr(word_num) in skip:
                count -= 1
            elif count == index:
                answer += chr(word_num)
                break
    return answer
