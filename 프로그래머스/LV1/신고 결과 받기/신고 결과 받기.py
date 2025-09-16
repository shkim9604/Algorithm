def solution(id_list, report, k):
    answer = []
    # 신고내역 key=유저 value=신고대상유저
    report_list = {}
    # 신고당한횟수 key=유저 value=신고당한횟수
    reported_list = {}
    for i in id_list:
        report_list[i] = []
        reported_list[i] = 0
    for i in report:
        i = i.split(" ")
        if i[1] in report_list[i[0]]:
            continue
        else:
            report_list[i[0]].append(i[1])
            reported_list[i[1]] += 1
    for i in report_list:
        complete_report_count = 0
        for j in report_list[i]:
            if reported_list[j] >= k:
                complete_report_count += 1
        answer.append(complete_report_count)
    return answer
