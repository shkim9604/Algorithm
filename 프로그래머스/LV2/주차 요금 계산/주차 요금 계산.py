def solution(fees, records):
    answer = []
    car_in = []
    in_record = {}
    parktime_record = {}
    for i in records:
        i = i.split(" ")
        if i[-1] == 'IN':
            car_in.append(i[1])
            time = i[0].split(":")
            time = int(time[0]) * 60 + int(time[1])
            in_record[i[1]] = time
        elif i[-1] == 'OUT':
            car_in.remove(i[1])
            time = i[0].split(":")
            time = int(time[0]) * 60 + int(time[1])
            park_time = time - in_record[i[1]]
            if i[1] not in parktime_record:
                parktime_record[i[1]] = park_time
            else:
                parktime_record[i[1]] += park_time
    if len(car_in) > 0:
        for i in car_in:
            time = 23 * 60 + 59
            park_time = time - in_record[i]
            if i not in parktime_record:
                parktime_record[i] = park_time
            else:
                parktime_record[i] += park_time

    parktime_record = dict(sorted(parktime_record.items()))
    print(f"주차시간: {parktime_record}")
    for i in parktime_record:
        if parktime_record[i] < fees[0]:
            park_money = fees[1]
            answer.append(park_money)
        else:
            basic_money = fees[1]
            extra_time = parktime_record[i] - fees[0]
            if extra_time % fees[2] != 0:
                extra_time = extra_time // fees[2] + 1
            else:
                extra_time //= fees[2]
            park_money = basic_money + extra_time * fees[-1]
            answer.append(park_money)

    return answer