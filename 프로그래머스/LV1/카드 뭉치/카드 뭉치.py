def solution(cards1, cards2, goal):
    answer = 'Yes'
    for i in goal:
        if i in cards1:
            if cards1[0] == i:
                del cards1[0]
            else:
                answer = "No"
                break
        elif i in cards2:
            if cards2[0] == i:
                del cards2[0]
            else:
                answer = "No"
                break
    return answer
