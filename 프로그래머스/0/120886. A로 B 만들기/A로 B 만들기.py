from collections import Counter
def solution(before, after):
    return 1 if Counter(before) == Counter(after) else 0