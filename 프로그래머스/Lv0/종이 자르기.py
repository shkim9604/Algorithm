def solution(M, N):
    answer = 0
    if M == 1 and N == 1:
        return 0
    M_count = M - 1
    N_count = (N - 1) * M
    answer = M_count + N_count
    return answer
