def solution(park, routes):
    answer = []
    start = []
    barricade = []
    w = len(park[0])
    h = len(park)
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                start.append(i)
                start.append(j)
            elif park[i][j] == 'X':
                barricade.append([i, j])
    for i in routes:
        i = i.split(" ")
        move_can = True
        if i[0] == 'E':
            # print(f"동쪽으로 {i[1]}번 움직여야함")
            count = 0
            for j in range(int(i[1])):
                start[1] += 1
                count += 1
                # print(f"동쪽으로 1이동 {start}")
                if start in barricade:
                    start[1] -= count
                    # print(f"장애물이 있어 움직인거 취소, 위치:{start}")
                    break
                elif start[1] >= w:
                    start[1] -= count
                    # print(f"공원내부를 벗어나서 취소, 위치:{start}")
                    break
        elif i[0] == 'W':
            count = 0
            for j in range(int(i[1])):
                start[1] -= 1
                count += 1
                # print(f"서쪽으로 1이동 {start}")
                if start in barricade:
                    start[1] += count
                    # print(f"장애물이 있어 움직인거 취소, 위치:{start}")
                    break
                elif start[1] < 0:
                    start[1] += count
                    # print(f"공원내부를 벗어나서 취소, 위치:{start}")
                    break
        elif i[0] == 'S':
            # print(f"남쪽으로 {i[1]}번 움직여야함")
            count = 0
            for j in range(int(i[1])):
                start[0] += 1
                count += 1
                # print(f"남쪽으로 1이동 {start}")
                if start in barricade:
                    start[0] -= count
                    # print(f"장애물이 있어 움직인거 취소, 위치:{start}")
                    break
                elif start[0] >= h:
                    start[0] -= count
                    # print(f"공원내부를 벗어나서 취소, 위치:{start}")
                    break
        else:
            # print(f"북쪽으로 {i[1]}번 움직여야함")
            count = 0
            for j in range(int(i[1])):
                start[0] -= 1
                count += 1
                # print(f"북쪽으로 1이동 {start}")
                if start in barricade:
                    start[0] += count
                    # print(f"장애물이 있어 움직인거 취소, 위치:{start}")
                    break
                elif start[0] < 0:
                    start[0] += count
                    # print(f"공원내부를 벗어나서 취소, 위치:{start}")
                    break
    answer = start
    return answer
