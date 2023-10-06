def solution(s):
    answer = True
    inner = 0
    outer = 0
    for val in list(s):
        if val == "(" : inner += 1
        else : outer += 1
        
        if inner < outer:
            answer = False
            break
    if inner != outer : answer = False
    return answer