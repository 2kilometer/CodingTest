import numpy as np
def solution(dots):
    dots = np.array(dots)
    return int((max(dots[:,0]) - min(dots[:,0])) * (max(dots[:,1]) - min(dots[:,1])))