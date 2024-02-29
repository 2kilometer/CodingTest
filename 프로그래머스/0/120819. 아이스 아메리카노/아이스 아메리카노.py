def solution(money):
    n = money//5500
    return [n, (money - 5500*n)]