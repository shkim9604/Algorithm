def solution(mats, park):
    answer = 0
    mats = list(sorted(mats, reverse=True))
    w = len(park[0])
    h = len(park)
    for i in mats:
        if answer == 0:
            for j in range(h - i + 1):
                for k in range(w - i + 1):
                    if park[j][k] == "-1":
                        can = True
                        for jj in range(j, j + i):
                            if can:
                                for kk in range(k, k + i):
                                    if park[jj][kk] == "-1":
                                        continue
                                    else:
                                        can = False
                                        break
                            else:
                                break
                        if can:
                            answer = i
                        else:
                            continue
        else:
            break
    if answer == 0:
        answer = -1

    return answer