import math
def solution(box, n):
    return math.prod([v//n for v in box])