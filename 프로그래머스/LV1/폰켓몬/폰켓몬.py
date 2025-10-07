def solution(nums):
    answer = 0
    mon_type = list(set(nums))
    for i in range(len(mon_type)):
        if answer == len(nums) // 2:
            break
        answer += 1
    return answer
