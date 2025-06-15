def solution(lines):
    answer = 0
    a = lines[0]
    b = lines[1]
    c = lines[2]
    overlap = []
    if max(a) > min(b):
        for i in range(a[0],a[1]):
            if i in range(b[0],b[1]):
                overlap.append(i)
    if max(a) > min(c):
        for i in range(a[0],a[1]):
            if i in range(c[0],c[1]):
                overlap.append(i)
    if max(b) > min(c):
        for i in range(b[0],b[1]):
            if i in range(c[0],c[1]):
                overlap.append(i)
    overlap = set(overlap)
    answer = len(overlap)
    return answer