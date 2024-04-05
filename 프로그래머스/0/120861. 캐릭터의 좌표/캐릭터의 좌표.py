import numpy as np
def solution(keyinput, board):
    x, y = 0, 0
    move = {'up':(0,1), 'down':(0,-1), 'left':(-1,0), 'right':(1,0)}
    
    for k in keyinput:
        dx, dy = move[k][0], move[k][1]
        if all([(abs(x+dx) <= board[0]//2), (abs(y+dy) <= board[1]//2)]):
            x, y = x+dx, y+dy

    return x, y