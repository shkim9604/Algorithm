def solution(answers):
    answer = []
    count = []
    one_pattern = [1, 2, 3, 4, 5]
    two_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    three_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one_count = 0
    two_count = 0
    three_count = 0
    for i in range(len(answers)):
        if answers[i] == one_pattern[i % len(one_pattern)]:
            one_count += 1
        if answers[i] == two_pattern[i % len(two_pattern)]:
            two_count += 1
        if answers[i] == three_pattern[i % len(three_pattern)]:
            three_count += 1
    count.append(one_count)
    count.append(two_count)
    count.append(three_count)
    if count.count(max(count)) >= 2:
        for i in range(len(count)):
            if count[i] == max(count):
                answer.append(i + 1)
    else:
        answer.append(count.index(max(count)) + 1)
    return answer
