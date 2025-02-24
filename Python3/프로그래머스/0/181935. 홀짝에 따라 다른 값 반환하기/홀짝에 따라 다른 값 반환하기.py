def solution(n):
    if n % 2 != 0:
        if n == 1:
            return 1
        return n + solution(n-2)
    
    if n % 2 == 0:
        if n == 2:
            return 2**2
        return n**2 + solution(n-2)