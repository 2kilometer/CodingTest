import itertools
def solution(numbers):
    comb = []
    for r in range(1, len(numbers)+1):
        comb += [int(''.join(v)) for v in itertools.permutations(numbers, r)]

    answer = 0
    for v in set(comb):
        if v in (0, 1): continue
        if v in (2,3,5,7) : 
            answer += 1
            continue
        for i in range(2, int(v**0.5)+1):
            if v%i == 0:
                break
            if i == int(v**0.5):
                answer += 1

    return answer