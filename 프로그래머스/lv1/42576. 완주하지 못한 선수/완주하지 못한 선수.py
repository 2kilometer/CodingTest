from collections import Counter
def solution(participant, completion):
    x_list = list(Counter(participant) - Counter(completion))
    return x_list[0]