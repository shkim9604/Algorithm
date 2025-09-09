def solution(schedules, timelogs, startday):
    answer = 0
    day = ["월", "화", "수", "목", "금", "토", "일"]
    for s, t in zip(schedules, timelogs):
        h = int(str(s)[:-2])
        m = int(str(s)[-2:])
        m += 10
        if m >= 60:
            h += 1
            m -= 60
        if m < 10:
            m = "0" + str(m)
        accept_time = int(f"{h}{m}")
        index = 0
        no_late = True
        for i in t:
            today = day[(startday - 1 + index) % len(day)]
            if today != "토" and today != "일":
                if i <= accept_time:
                    index += 1
                    pass
                else:
                    no_late = False
                    break
            else:
                index += 1
        if no_late:
            answer += 1
    return answer
