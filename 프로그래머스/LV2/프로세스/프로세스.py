def solution(priorities, location):
    answer = 1
    index = priorities.index(max(priorities))
    while True:
        if index >= len(priorities):
            index -= len(priorities)
        if priorities[index] == max(priorities) and index == location:
            break
        elif priorities[index] == max(priorities):
            priorities[index] = -1
            index += 1
            answer += 1
        else:
            index += 1

    return answer
