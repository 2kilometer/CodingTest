def solution(lines):
    answer = 0
    for i, [l1, l2] in enumerate(lines):
        cmpr = lines[(i+1)%3]
        answer += max(len(set(range(l1, l2+1)) & set(range(cmpr[0], cmpr[1]+1)))-1, 0)
        
        if i == 2:
            cmpr2 = lines[(i+2)%3]
            answer -= max((len(set(range(l1, l2+1)) & set(range(cmpr[0], cmpr[1]+1)) &\
                              set(range(cmpr2[0], cmpr2[1]+1)))-1)*2, 0)
    return answer