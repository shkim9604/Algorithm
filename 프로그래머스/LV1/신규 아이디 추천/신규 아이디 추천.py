import re


def solution(new_id):
    answer = ''
    # 1 step
    new_id = new_id.lower()

    # 2 step
    pattern = re.compile('[^a-z0-9_.-]')
    new_id = pattern.sub('', new_id)

    # 3 step
    pattern = re.compile('[.]{2,}')
    new_id = pattern.sub('.', new_id)

    # 4 step
    if new_id == '':
        pass
    else:
        if new_id[0] == '.' and new_id[-1] == '.':
            new_id = new_id[:-1]
            new_id = new_id.replace('.', '', 1)
        elif new_id[0] == '.':
            new_id = new_id.replace('.', '', 1)
        elif new_id[-1] == '.':
            new_id = new_id[:-1]

    # 5 step
    if new_id == '':
        new_id += 'a'

    # 6 step
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7 step
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]

    answer = new_id
    return answer
