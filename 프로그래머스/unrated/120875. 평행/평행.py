from itertools import combinations, permutations
def solution(dots):
    inclins = []
    y_inters = []
    for set1, set2 in (combinations(combinations(dots, 2), 2)):
        set1_2 = set(map(tuple, set1 + set2))
        if len(set1+set2)-len(set1_2): continue
        else:
            inclin_1 = (set1[0][1]-set1[1][1])/(set1[0][0]-set1[1][0])
            inclin_2 = (set2[0][1]-set2[1][1])/(set2[0][0]-set2[1][0])
            print(inclin_1, inclin_2)
            if inclin_1 == inclin_2: 
                answer = 1
                break
            else : answer = 0
    
    return answer