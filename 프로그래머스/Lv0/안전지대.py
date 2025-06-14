def solution(board):
    answer = 0
    bomb_loc = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                bomb_loc.append([i, j])
    danger = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
    for i in bomb_loc:
        bomb = i
        for j in danger:
            x = bomb[0] - j[0]
            y = bomb[1] - j[1]
            if x < 0:
                x = 0
            elif x > len(board) - 1:
                x = len(board) - 1
            if y < 0:
                y = 0
            elif y > len(board[0]) - 1:
                y = len(board[0]) - 1
            board[x][y] = 1
    for i in board:
        answer += i.count(0)
    return answer
