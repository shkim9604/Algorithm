def solution(s):
    answer = 0
    start_word = ''
    slice_word = ''
    another_count = 0
    count = 0
    for i in range(len(s)):
        if start_word == '':
            start_word = s[i]
            count += 1
            slice_word += s[i]
            continue
        if start_word != s[i]:
            another_count += 1
            slice_word += s[i]
            if count == another_count:
                start_word = ''
                count = 0
                another_count = 0
                slice_word = ''
                answer += 1
        elif start_word == s[i]:
            count += 1
            slice_word += s[i]
    if slice_word != '':
        answer += 1
    return answer
