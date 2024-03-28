from functools import reduce
def solution(str1, str2):
    return ''.join(reduce(lambda a,b: a+b, zip(str1, str2)))