def solution(sizes):
    w, h = 0, 0    
    for s in sizes:
        w, h = max(max(s), w), max(min(s), h)
    
    return w*h