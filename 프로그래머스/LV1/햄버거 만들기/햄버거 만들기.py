def solution(ingredient):
    answer = 0
    material = ''

    for i in ingredient:
        material += str(i)
        if material[-4:] == '1231':
            answer += 1
            material = material[:-4]
    return answer
