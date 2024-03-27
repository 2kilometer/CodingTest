def solution(prices):
    answer = []
    for i in range(0, len(prices)-1):
        step_idx = 0
        for j in range(i+1, len(prices)):
            
            if prices[i] <= prices[j]:
                step_idx = j
            else:
                step_idx = j
                break
        answer.append(step_idx - i)
    return answer + [0]