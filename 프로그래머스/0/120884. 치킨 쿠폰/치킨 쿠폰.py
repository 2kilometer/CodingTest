def solution(chicken):
    answer = 0
    
    while chicken >= 10:  
        coupon = chicken//10
        left = chicken%10
        
        answer += coupon
        chicken = coupon + left
        
    return answer