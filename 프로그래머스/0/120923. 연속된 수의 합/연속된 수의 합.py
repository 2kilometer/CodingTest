from math import ceil
def solution(num, total):
    return list(range(ceil(total/num)-num//2, ceil(total/num)-num//2 + num))