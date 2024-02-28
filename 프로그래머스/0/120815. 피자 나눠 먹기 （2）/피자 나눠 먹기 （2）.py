def solution(n):
    cnt = 1
    while 1:
        if (cnt*6) % n == 0: break
        else: cnt += 1
    return cnt