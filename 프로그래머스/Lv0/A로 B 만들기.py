def solution(before, after):
    answer = 0
    set_before = list(set(before))
    set_after = list(set(after))
    set_before.sort()
    set_after.sort()
    before_count = dict()
    after_count = dict()
    for i in set_before:
        before_count[i] = before.count(i)
    for i in set_after:
        after_count[i] = after.count(i)

    for b, a in zip(before_count, after_count):
        if b == a:
            if before_count[b] == after_count[a]:
                answer = 1
            else:
                answer = 0
                break
        else:
            answer = 0
            break
    return answer
