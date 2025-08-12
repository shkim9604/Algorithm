def solution(keymap, targets):
    answer = []
    for i in targets:
        hap = 0
        for j in i:
            h_count = 200
            for k in range(len(keymap)):
                try:
                    k_count = keymap[k].index(j) + 1
                    h_count = min(k_count, h_count)
                except:
                    pass
            if h_count == 200:
                break
            hap += h_count

        if h_count == 200:
            answer.append(-1)
        else:
            answer.append(hap)
    return answer
