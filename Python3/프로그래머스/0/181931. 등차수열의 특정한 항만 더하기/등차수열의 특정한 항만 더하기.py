def solution(a, d, included):
    answer = 0
    return sum([a + (d * i) for i in range(len(included)) if included[i]])