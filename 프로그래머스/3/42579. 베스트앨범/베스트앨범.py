def solution(genres, plays):
    idx_dict = {}
    cnt_dict = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g in idx_dict.keys():
            if len(idx_dict[g]) < 2:                
                if p > cnt_dict[g][0]:
                    idx_dict[g].insert(0, i)
                    cnt_dict[g].insert(0, p)
                else:
                    idx_dict[g] += [i]
                    cnt_dict[g] += [p]
            else:
                if p > cnt_dict[g][0]:
                    idx_dict[g].insert(0, i)
                    cnt_dict[g].insert(0, p)
                elif p > cnt_dict[g][1]:
                    idx_dict[g].insert(1, i)
                    cnt_dict[g].insert(1, p)
                else:
                    cnt_dict[g] += [p]
                
        else:
            idx_dict[g] = [i]
            cnt_dict[g] = [p]
            
    answer = []
    for k in sorted(cnt_dict, key=lambda x: sum(cnt_dict[x]), reverse=True):
        answer += idx_dict[k][:2]
        
    return answer