def solution(numbers, k):
    idx = 0
    for _ in range(k-1):
        idx += 2
        if idx > len(numbers)-1:
            idx %= len(numbers)
    return numbers[idx]