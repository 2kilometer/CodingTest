def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(n-x), -x))