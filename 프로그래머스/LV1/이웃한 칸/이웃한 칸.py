def solution(board, h, w):
    answer = 0
    area = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    for i in area:
        a_h = h + i[0]
        a_w = w + i[-1]
        if a_h < 0 or a_w < 0 or a_h >= len(board) or a_w >= len(board):
            continue
        if board[h][w] == board[a_h][a_w]:
            answer += 1
    return answer
