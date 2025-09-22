from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    count = count.most_common()
    box = 0
    for i in count:
        answer += 1
        box += i[1]
        if box >= k:
            break

    return answer
