def solution(array, height):
    return sum(1 for a in array if a > height)