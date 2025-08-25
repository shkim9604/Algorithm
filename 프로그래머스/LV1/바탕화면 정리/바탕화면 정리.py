def solution(wallpaper):
    answer = []
    left_xy = [50, 50]
    right_xy = [0, 0]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                left_xy[0] = min(left_xy[0], i)
                left_xy[1] = min(left_xy[1], j)
                right_xy[0] = max(right_xy[0], i)
                right_xy[1] = max(right_xy[1], j)
    for i in left_xy:
        answer.append(i)
    for i in right_xy:
        answer.append(i + 1)
    return answer
