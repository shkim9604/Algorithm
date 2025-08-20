def solution(board, moves):
    answer = 0
    pocket = []
    for i in moves:
        for j in range(len(board[i - 1])):
            if board[j][i - 1] != 0:
                pocket.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
        if len(pocket) >= 2:
            if pocket[-1] == pocket[-2]:
                answer += 2
                pocket.pop()
                pocket.pop()
        else:
            continue

    return answer
