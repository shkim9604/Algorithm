def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(0, len(phone_book) - 1):
        num = phone_book[i]
        if num == phone_book[i + 1][:len(num)]:
            return False

    return answer
