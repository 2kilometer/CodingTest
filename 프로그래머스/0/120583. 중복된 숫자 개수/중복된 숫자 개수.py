def solution(array, n):
    return str(array).replace('[',' ').replace(']',',').count(' '+str(n)+',')