def solution(A, B):
    def comp(i):
        idx = len(A)-(i)
        if A[idx:]+A[:idx] == B:
            return i
        else:
            if i == len(A)-1:
                return -1
            else:
                return comp(i+1)

    return comp(0)