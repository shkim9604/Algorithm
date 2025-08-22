def solution(numbers, hand):
    answer = ''
    num_loc = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2],'*': [3, 0], 0: [3, 1], '#': [3, 2]}
    left_push = [1, 4, 7]
    right_push = [3, 6, 9]
    middle_push = [2, 5, 8, 0]
    left_loc = '*'
    right_loc = '#'
    for i in numbers:
        if i in left_push:
            answer += "L"
            left_loc = i
        elif i in right_push:
            answer += 'R'
            right_loc = i
        elif i in middle_push:
            left_pos = num_loc[left_loc]
            right_pos = num_loc[right_loc]
            num_pos = num_loc[i]
            left_range = abs(num_pos[1] - left_pos[1]) + abs(num_pos[0] - left_pos[0])
            right_range = abs(num_pos[1] - right_pos[1]) + abs(num_pos[0] - right_pos[0])
            if left_range < right_range:
                answer += 'L'
                left_loc = i
            elif left_range > right_range:
                answer += 'R'
                right_loc = i
            elif left_range == right_range:
                if hand == 'left':
                    answer += 'L'
                    left_loc = i
                else:
                    answer += 'R'
                    right_loc = i
    return answer
