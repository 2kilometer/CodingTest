from collections import deque
def solution(n, computers):
    answer = sum([1 for i in range(n) if (sum(computers[i]) == 1)])
    
    for i in range(n):
        if sum(computers[i]) == 1:
            continue
        answer += 1
        q = deque([i])
        while q:
            node = q.popleft()
            for j in range(n):
                if node == j:
                    continue
                if computers[node][j] == 1:
                    q.append(j)
                    computers[node][j] = 0
                    computers[j][node] = 0
        
    return answer