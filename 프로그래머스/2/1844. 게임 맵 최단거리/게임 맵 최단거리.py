from collections import deque
def solution(maps):
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if any([(nx<0), (nx>=n), (ny<0), (ny>=m)]):
                    continue
            
                if maps[nx][ny] == 0:
                    continue

                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
            
        return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
            
    m, n = len(maps[0]), len(maps)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    return bfs(0, 0)