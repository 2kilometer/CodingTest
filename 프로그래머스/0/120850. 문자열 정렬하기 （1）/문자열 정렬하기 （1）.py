import re
def solution(my_string):
    my_string = list(map(int, re.findall(r'\d', my_string)))
    return sorted(my_string)