def solution(numbers, hand):
    loc={1:(1,1),2:(1,2),3:(1,3),4:(2,1),5:(2,2),6:(2,3),7:(3,1),8:(3,2),9:(3,3),0:(4,2),"*":(4,1),"#":(4,3)}
    
    h_left = "*"
    h_right = "#"
    result = ""
    
    for num in numbers:
        if num in (1,4,7):
            result += "L"
            h_left = num
        elif num in (3,6,9):
            result += "R"
            h_right = num
        else :
            l_h11,l_h12,l_h21,l_h22 = loc[h_left]+loc[num]
            r_h11,r_h12,r_h21,r_h22 = loc[h_right]+loc[num]
            l_loc = abs(l_h11-l_h21)+abs(l_h12-l_h22)
            r_loc = abs(r_h11-r_h21)+abs(r_h12-r_h22)
            
            if l_loc < r_loc :
                result += "L"
                h_left = num
            elif l_loc > r_loc :
                result += "R"
                h_right = num
            else: 
                if hand == "left" :
                    result += "L"
                    h_left = num
                elif hand == "right"  :
                    result += "R"
                    h_right = num
    
    return result