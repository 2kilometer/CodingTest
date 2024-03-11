def solution(my_string, num1, num2):
    _min = min(num1, num2)
    _max = max(num1, num2)        
    return my_string[:_min]+my_string[_max]+my_string[_min+1:_max]+my_string[_min]+my_string[_max+1:]