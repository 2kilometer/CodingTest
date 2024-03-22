from functools import cmp_to_key, reduce
def compare(x, y):
    if str(x)+str(y) >= str(y)+str(x):
    	return -1
    else:
    	return 1

def solution(numbers):
    answer = sorted(numbers, key=cmp_to_key(compare))
    if set(answer) == {0}:
        return "0"
    else:
        return "".join([str(v) for v in answer])