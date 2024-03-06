def solution(s):
    answer = 0
    s = s.split(' ')
    for i in range(len(s)):
        if s[i] == 'Z' : 
            answer -= int(s[i-1])
        else: answer += int(s[i])
 
    return answer