def solution(number, n, m):
    return 1 if all([(number%n == 0), (number%m ==0)]) else 0