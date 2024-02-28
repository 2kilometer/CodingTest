def solution(n):
    cnt = 1
    while cnt * 6 % n:
        cnt += 1
        
    return cnt