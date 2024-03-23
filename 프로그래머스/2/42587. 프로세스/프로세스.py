from collections import deque
def solution(priorities, location):
    answer = []
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    while len(queue) > 1:
        if queue[0][0] >= max(queue)[0]:
            answer.append(queue.popleft()[1])
            if len(queue) == 1:
                answer.append(queue[0][1])
        else:
            queue.rotate(-1)
    
    return answer.index(location)+1