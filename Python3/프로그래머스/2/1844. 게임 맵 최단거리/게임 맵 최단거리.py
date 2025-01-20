from collections import deque
def solution(maps):
    n = len(maps) - 1
    m = len(maps[0]) -1
    if (maps[n-1][m] == 0) and (maps[n][m-1] == 0):
        return -1
    
    answer, queue = 0, deque([[0, 0]])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        if x == n and y == m:
            return maps[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx <= n) and (0 <= ny <= m):                    
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append([nx, ny])
        
    return -1