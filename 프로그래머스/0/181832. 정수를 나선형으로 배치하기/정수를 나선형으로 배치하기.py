import numpy as np
def solution(n):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x, y, r = 0, 0, 0   
    answer = np.full((n,n), 0)
    
    for num in range(1, (n**2+1)):
        answer[x][y] = num
        nx = x + dx[r%4]
        ny = y + dy[r%4]
        
        if any([(nx==n), (ny==n), (ny < 0), (answer[nx:nx+1, ny:ny+1] != 0)]):
            r += 1
            x += dx[r%4]
            y += dy[r%4]
            continue
        x, y = nx, ny
    return answer.tolist()