def solution(keymap, targets):
    key_nums = {}
    for key in keymap:
        for i, k in enumerate(key):
            if not (key_nums.get(k)) or (i+1 < key_nums.get(k)):
                key_nums[k] = i+1
                
    answer = []
    
    for target in targets:
        if set(target) - set(key_nums):
            answer.append(-1)
            continue
            
        cnt = 0
        for letter in target:
            if key_nums.get(letter):
                cnt += key_nums.get(letter)
                
        answer.append(cnt)
            
    return answer