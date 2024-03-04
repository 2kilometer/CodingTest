def solution(emergency):
    _sorted = sorted(emergency, reverse=True)    
    return [_sorted.index(v)+1 for v in emergency]