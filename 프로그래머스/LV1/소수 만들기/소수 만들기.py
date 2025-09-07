def solution(nums):
    answer = 0

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                count = nums[i] + nums[j] + nums[k]
                prime = True
                for c in range(2, int(count ** 0.5) + 1):
                    if count % c == 0:
                        prime = False
                        break
                if prime:
                    answer += 1

    return answer
