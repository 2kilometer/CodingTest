def solution(str1, str2):  
    return ''.join([a+b for a,b in zip(list(str1), list(str2))])