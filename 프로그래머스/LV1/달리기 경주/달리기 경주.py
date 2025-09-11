def solution(players, callings):
    answer = []
    rank = {}
    for i in range(len(players)):
        rank[players[i]] = i
    for i in callings:
        call_rank = rank[i]
        before_player = players[call_rank - 1]
        players[call_rank - 1] = i
        players[call_rank] = before_player

        rank[players[call_rank]] = call_rank
        rank[players[call_rank - 1]] = call_rank - 1

    answer = players

    return answer
