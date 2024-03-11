def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer += [n//i, i]

    return sorted(set(answer))