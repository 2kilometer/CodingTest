def solution(sides):
    sides.sort()
    max_last = len(range(sides[1]-sides[0]+1, sides[1]+1))
    max_othr = len(range(sides[1]+1, sum(sides)))
    return max_last + max_othr