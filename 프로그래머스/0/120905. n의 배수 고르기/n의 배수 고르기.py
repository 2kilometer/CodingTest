def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))