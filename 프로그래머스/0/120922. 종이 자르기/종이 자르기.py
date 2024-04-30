def solution(M, N):
    return (min(M, N)-1) + (max(M, N)-1)*min(M, N)