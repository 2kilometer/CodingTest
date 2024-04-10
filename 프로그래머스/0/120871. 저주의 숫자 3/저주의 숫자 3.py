def solution(n):
    i, x3 = 1, 1
    while x3 <= n:
        if n == 1:
            return 1
        i += 1
        if not any([(i%3==0), ('3' in str(i))]):
            x3 += 1
            if x3 == n:
                return i
