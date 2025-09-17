def solution(bandage, health, attacks):
    answer = 0
    max_health = health  # 최대체력 저장
    t = bandage[0]  # 시전시간
    x = bandage[1]  # 초당 회복량
    y = bandage[2]  # 추가 회복량
    success = 0  # 연속성공횟수
    time_damage = {}
    attack_time = []
    for i in attacks:
        time_damage[i[0]] = i[1]
        attack_time.append(i[0])
    max_time = max(attack_time)
    for i in range(1, max_time + 1):
        if i in attack_time:
            # 공격O 회복 불가능
            damage = time_damage[i]
            success = 0
            health -= damage
            if health <= 0:
                break
        else:
            # 공격X 회복가능
            success += 1
            if success == t:
                health += x + y
                success = 0
                if health >= max_health:
                    health = max_health
            else:
                health += x
                if health >= max_health:
                    health = max_health

    if health <= 0:
        answer = -1
    else:
        answer = health
    return answer
