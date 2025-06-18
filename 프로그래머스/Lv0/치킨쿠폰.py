def solution(chicken):
    answer = 0
    chicken_service = 0
    coupon = chicken
    while coupon >= 10:
        chicken_service = coupon // 10
        answer += chicken_service
        coupon %= 10
        coupon += chicken_service

    return answer
