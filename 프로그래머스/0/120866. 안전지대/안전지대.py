import numpy as np
def solution(board):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    n = len(board)
    np_board = np.array(board)
    
    def fill_2(x, y):       
        for i in range(8):
            next_x = x+dx[i]
            next_y = y+dy[i]
            if 0<=next_x<n and 0<=next_y<n:
                np_board[next_x][next_y] = 2

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                fill_2(i, j)
                np_board[i][j] = 2
    
    return int(n**2 - np.sum(np_board)/2)