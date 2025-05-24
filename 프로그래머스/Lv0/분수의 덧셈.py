import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    n = numer1 * denom2 + numer2 * denom1
    d = denom1 * denom2
    a = math.gcd(n,d)
    n = n // a
    d = d // a
    answer.append(n)
    answer.append(d)
    return answer
