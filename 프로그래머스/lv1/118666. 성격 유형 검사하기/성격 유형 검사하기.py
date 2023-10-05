from collections import Counter
def solution(survey, choices):   
    temp = []
    for i in range(len(choices)):
        if choices[i] == 4 :
            continue
        elif choices[i] < 4 :
            temp += [survey[i][0]] * (4-choices[i])
        else :
            temp += [survey[i][1]] * (choices[i]-4)
    
    a = Counter(temp)
    prsnty = ""
    if a["R"] >= a["T"] : prsnty += "R"
    else : prsnty += "T"
    if a["C"] >= a["F"] : prsnty += "C"
    else : prsnty += "F"
    if a["J"] >= a["M"] : prsnty += "J"
    else : prsnty += "M"
    if a["A"] >= a["N"] : prsnty += "A"
    else : prsnty += "N"

    return prsnty