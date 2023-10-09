def solution(answers):
    p_1 = [1, 2, 3, 4, 5] 
    p_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = {1:0, 2:0, 3:0}
    for i in range(len(answers)):
        if answers[i] == p_1[i%5]: cnt[1] += 1
        if answers[i] == p_2[i%8]: cnt[2] += 1
        if answers[i] == p_3[i%10]: cnt[3] += 1
        
    answer = list(filter(lambda k: cnt[k] == max(cnt.values()), cnt.keys()))
        
    return answer