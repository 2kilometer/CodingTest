def solution(common):
    gap1 = common[1]-common[0]
    gap2 = common[2]-common[1]
    
    return (common[-1]+gap1) if gap1 == gap2 else (common[-1]*(gap2//gap1))