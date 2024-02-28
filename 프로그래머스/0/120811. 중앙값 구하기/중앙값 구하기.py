# 메모리: 10.2 MB, 시간: 0.00 ms
def solution(array):
    return sorted(array)[len(array) // 2]

# 메모리: 28.6 MB, 시간: 0.24 ms
import numpy as np
def solution(array):
    return np.median(array)

# 메모리: 28.8 MB, 시간: 0.17 ms
import numpy as np
solution = lambda array: np.median(array)
