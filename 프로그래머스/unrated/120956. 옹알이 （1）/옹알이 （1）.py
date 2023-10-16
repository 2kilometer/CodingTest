from itertools import permutations
def solution(babbling):
    bablings = ["aya", "ye", "woo", "ma"]
    bablings_2 = ["".join(v) for v in list(permutations(bablings, 2))]
    bablings_3 = ["".join(v) for v in list(permutations(bablings, 3))]
    bablings_4 = ["".join(v) for v in list(permutations(bablings, 4))]
    bablings += bablings_2
    bablings += bablings_3
    bablings += bablings_4
    
    answer = len([b for b in babbling if b in bablings])
    return answer