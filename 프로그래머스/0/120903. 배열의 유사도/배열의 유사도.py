def solution(s1, s2):
    answer = 0
    if len(s1) != len(set(s1)-set(s2)):
        answer = len(s1) - len(set(s1)-set(s2))
    return answer