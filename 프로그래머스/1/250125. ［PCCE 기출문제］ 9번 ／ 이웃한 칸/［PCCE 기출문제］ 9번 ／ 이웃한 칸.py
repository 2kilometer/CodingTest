def solution(board, h, w):
    n = len(board)
    dh = [0, 0, 1, -1]
    dw = [1, -1, 0, 0]
    answer = 0
    
    for i in range(len(dh)):
        nh = h + dh[i]
        nw = w + dw[i]
        
        if all([(0 <= nh < n), (0 <= nw < n)]):
            if board[h][w] == board[nh][nw]:
                answer += 1
                
    return answer