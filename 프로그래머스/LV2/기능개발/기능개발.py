def solution(progresses, speeds):
    answer = []
    index = 0
    count = 0
    while index < len(speeds):
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        while True:
            if index < len(speeds) and progresses[index] >= 100:
                count += 1
                index += 1
            else:
                break
        if count != 0:
            answer.append(count)
            count = 0

    return answer
