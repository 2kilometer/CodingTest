import math
def solution(progresses, speeds):
    release = [math.ceil((100-p)/s) for p, s in zip(progresses,speeds)]
    
    prog_point = 0
    answer = []
    for i, r in enumerate(release):
        if i == 0 : continue
        if r > release[prog_point]:
            answer += [i - prog_point]
            prog_point = i
    answer += [len(release)-prog_point]
            
    return answer