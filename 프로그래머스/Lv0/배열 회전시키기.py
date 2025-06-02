def solution(numbers, direction):
    answer = []
    if direction == "right":
        num = numbers[-1]
        numbers.pop()
        numbers.insert(0,num)
    elif direction == 'left':
        num = numbers[0]
        numbers.remove(numbers[0])
        numbers.append(num)
    answer = numbers
    return answer
