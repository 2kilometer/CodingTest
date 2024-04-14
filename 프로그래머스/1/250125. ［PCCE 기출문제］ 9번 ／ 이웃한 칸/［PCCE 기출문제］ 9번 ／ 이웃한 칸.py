def solution(board, h, w):
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    n = len(board)
    answer = 0
    
    for i in range(4):
        if all([(h+dh[i]>=0), (h+dh[i]<n), (w+dw[i]>=0), (w+dw[i]<n)]):
            if board[h][w] == board[h+dh[i]][w+dw[i]]:
                answer += 1
    return answer