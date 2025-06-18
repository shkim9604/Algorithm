def solution(bin1, bin2):
    answer = ''
    bin1 = "0b" + bin1
    bin2 = "0b" + bin2
    x = int(bin1, 2)
    y = int(bin2, 2)
    answer = bin(x + y)
    answer = answer[2:]
    return answer
