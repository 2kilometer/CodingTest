def solution(array, commands):
    answer=[]
    
    for cmd in commands:
        start = cmd[0]-1
        idx = cmd[2]-1
        answer += [sorted(array[start:cmd[1]])[idx]]
    
    return answer