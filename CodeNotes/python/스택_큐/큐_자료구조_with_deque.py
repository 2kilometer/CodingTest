"""
deque 라이브러리 사용 시, list로 queue 구현했을 때 보다 시간복잡도가 줄어듦
-> deque의 append, popleft : O(1)
"""

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
