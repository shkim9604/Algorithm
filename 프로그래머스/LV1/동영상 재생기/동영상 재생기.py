def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    c_time = int(pos.split(":")[0]) * 60 + int(pos.split(":")[1])
    start_time = int(op_start.split(":")[0]) * 60 + int(op_start.split(":")[1])
    end_time = int(op_end.split(":")[0]) * 60 + int(op_end.split(":")[1])
    max_time = int(video_len.split(":")[0]) * 60 + int(video_len.split(":")[1])

    for i in commands:
        if start_time <= c_time <= end_time:
            c_time = end_time
        if i == 'next':
            c_time += 10
            if c_time > max_time:
                c_time = max_time
            elif start_time <= c_time <= end_time:
                c_time = end_time
        elif i == 'prev':
            c_time -= 10
            if c_time < 0:
                c_time = 0
            elif start_time <= c_time <= end_time:
                c_time = end_time

    if start_time <= c_time <= end_time:
        c_time = end_time

    minute = c_time // 60
    second = c_time % 60
    answer = str(minute).zfill(2) + ":" + str(second).zfill(2)

    return answer