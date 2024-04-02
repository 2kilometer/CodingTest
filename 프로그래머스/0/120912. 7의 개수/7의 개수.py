import re
def solution(array):
    return sum(len(re.findall('7', str(v))) for v in array)