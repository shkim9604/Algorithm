def solution(n, w, num):
    answer = 1
    pos = []
    if n % w != 0:
        line = n // w + 1
    else:
        line = n // w
    storage = []
    box = []
    loc = 0
    for i in range(line):
        if i % 2 == 0:
            for j in range(w):
                if i * w + j + 1 > n:
                    box.append(0)
                else:
                    box.append(i * w + j + 1)
            if num in box:
                loc = box.index(num)
                pos = [i, loc]
            if box:
                storage.append(box)
                box = []
        else:
            for j in range(w - 1, -1, -1):
                if i * w + j + 1 > n:
                    box.append(0)
                else:
                    box.append(i * w + j + 1)
            if num in box:
                loc = box.index(num)
                pos = [i, loc]
            if box:
                storage.append(box)
                box = []

    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if j == pos[1] and storage[i][j] != 0 and storage[i][j] > num:
                answer += 1

    return answer
