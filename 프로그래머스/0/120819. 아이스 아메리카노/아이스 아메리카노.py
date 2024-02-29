def solution(money):
    n = money//5500
    answer = [n, (money - 5500*n)]
    return answer