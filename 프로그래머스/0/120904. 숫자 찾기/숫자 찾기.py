def solution(num, k):
    for i, v in enumerate(str(num)):
        if int(v) == k:
            return i+1
    return -1 