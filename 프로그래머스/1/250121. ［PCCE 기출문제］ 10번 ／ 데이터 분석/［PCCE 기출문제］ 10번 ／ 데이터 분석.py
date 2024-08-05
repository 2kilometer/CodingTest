def solution(data, ext, val_ext, sort_by):
    answer = []
    
    cols = ["code", "date", "maximum", "remain"]
    ext_idx = cols.index(ext)
    sort_idx = cols.index(sort_by)
    
    for d in data:
        if d[ext_idx] < val_ext:
            answer.append(d)
            
    answer.sort(key=lambda x: x[sort_idx])       
    
    return answer