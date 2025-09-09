def solution(want, number, discount):
    answer = 0
    purchase = {}
    for w,n in zip(want, number):
        purchase[w] = n
    purchase = dict(sorted(purchase.items()))
    for i in range(0,len(discount)-9):
        can_purchase = {}
        p_list = discount[i:i+10]
        for j in want:
            can_purchase[j] = p_list.count(j)
        can_purchase = dict(sorted(can_purchase.items()))
        can_buy = True
        for a,b in zip(purchase,can_purchase):
            if purchase[a] != can_purchase[b]:
                can_buy = False
                break
        if can_buy:
            answer +=  1
    return answer