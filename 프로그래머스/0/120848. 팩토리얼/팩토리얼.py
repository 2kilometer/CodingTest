import math
def solution(n):
    for i in range(10,0,-1):
        fact = math.factorial(i)
        if max(n, fact) == n:
            return i