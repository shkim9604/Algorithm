def solution(a, b):
    answer = ''
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    day_count = sum(months[:a-1]) + b - 1
    day = day_count % 7
    answer = days[day]

    return answer
