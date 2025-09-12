def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split(".")))
    year = today[0]
    month = today[1]
    day = today[2]
    condition = {}
    for i in terms:
        i = i.split(" ")
        condition[i[0]] = int(i[1])
    for i in range(len(privacies)):
        p_data = privacies[i]
        p_data = p_data.split(" ")
        stamp = p_data[1]
        e_date = list(map(int, p_data[0].split(".")))
        e_year = e_date[0]
        e_month = e_date[1]
        e_day = e_date[2]
        e_month += condition[stamp]
        print(e_month)
        if e_month > 12:
            e_year += (e_month - 1) // 12
            e_month = (e_month - 1) % 12 + 1
        e_day -= 1
        if e_day <= 0:
            e_day = 28
            e_month -= 1
            if e_month <= 0:
                e_month = 12
                e_year -= 1
        if e_year < year:
            answer.append(i + 1)
        elif e_year == year and e_month < month:
            answer.append(i + 1)
        elif e_year == year and e_month == month and e_day < day:
            answer.append(i + 1)

    return answer
