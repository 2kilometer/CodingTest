def solution(s):    
    return ''.join(sorted(v for v in set(s) if s.count(v) == 1))