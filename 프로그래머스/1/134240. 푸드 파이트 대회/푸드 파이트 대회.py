def solution(food):
    food_desc = food[::-1]
    food_set = ['0']
    n = len(food) - 1
    
    for i, f in enumerate(food_desc[:-1]):
        if (f//2) != 0 :
            food_set.append(str(n-i)*(f//2))
            food_set.insert(0, str(n-i)*(f//2))
            
    answer = "".join(food_set)        
    
    return answer