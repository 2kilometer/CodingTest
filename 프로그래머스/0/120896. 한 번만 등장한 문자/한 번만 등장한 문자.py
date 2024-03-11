from collections import Counter
def solution(s):
    answer = []
    for k, v in Counter(s).items():
        if v == 1:
            answer.append(k)
    
    return ''.join(sorted(answer))