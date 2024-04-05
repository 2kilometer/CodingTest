import numpy as np
def solution(keyinput, board):
    x, y = 0, 0
    move = {'up':[0,1], 'down':[0,-1], 'left':[-1,0], 'right':[1,0]}
    
    for k in keyinput:
        x += move[k][0]
        y += move[k][1]
        if any([(abs(x)>board[0]//2), (abs(y)>board[1]//2)]):
            x -= move[k][0]
            y -= move[k][1]

    
    return x, y