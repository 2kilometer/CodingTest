import math
def solution(num_list):
    if math.prod(num_list) < sum(num_list) ** 2:
        return 1
    return 0