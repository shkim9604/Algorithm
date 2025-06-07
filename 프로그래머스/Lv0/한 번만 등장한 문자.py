def solution(s):
    answer = ''
    show = []
    one_show = []
    for i in s:
        if i not in show:
            show.append(i)
            one_show.append(i)
        else:
            if i in one_show:
                one_show.remove(i)
    one_show.sort()
    answer = answer.join(one_show)
    return answer
