def solution(n):
    return sum(int(str(n)[i]) for i in range(len(str(n))))