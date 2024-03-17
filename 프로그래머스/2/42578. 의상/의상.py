from math import prod
import numpy as np
from collections import Counter

def solution(clothes):
    clth_cnt = Counter(np.array(clothes)[:,1])
    
    return prod(map(lambda x: x+1, clth_cnt.values()))-1