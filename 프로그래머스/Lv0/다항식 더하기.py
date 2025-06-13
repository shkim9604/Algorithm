def solution(polynomial):
    answer = ''
    polynomial = polynomial.split("+")
    x_in = []
    num = []
    for i in polynomial:
        if 'x' in i:
            x_in.append(i)
        else:
            num.append(i)
    x_count = 0
    num_count = 0
    for i in x_in:
        i = i.strip()
        if len(i) > 1:
            i = i.split("x")
            x_count += int(i[0])
        else:
            x_count += 1
    for i in num:
        num_count += int(i)
    if x_count > 1 and num_count > 0:
        answer = f"{x_count}x + {num_count}"
    elif x_count > 1 and num_count <= 0:
        answer = f"{x_count}x"
    elif x_count == 1 and num_count > 0:
        answer = f"x + {num_count}"
    elif x_count == 1 and num_count <= 0:
        answer = "x"
    elif x_count < 1 and num_count > 0:
        answer = f"{num_count}"

    return answer
