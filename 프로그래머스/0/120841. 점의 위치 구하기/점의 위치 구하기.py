def solution(dot):
    space = {(0,0):1, (1,0):2, (1,1):3, (0,1):4}
    dot = tuple(0 if v>0 else 1 for v in dot)
    
    return space[dot]