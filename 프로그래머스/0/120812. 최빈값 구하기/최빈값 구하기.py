from collections import Counter
def solution(array):
    cnt = Counter(array)
    answer = cnt.most_common(2)[0][0]
    
    if (len(cnt.most_common(2))==2):
        if (cnt.most_common(2)[0][1] == cnt.most_common(2)[1][1]):
            answer = -1
    
    return answer