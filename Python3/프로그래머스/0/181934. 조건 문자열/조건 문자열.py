def solution(ineq, eq, n, m):
    if ineq == ">":
        n, m = m, n
    if eq == "=":
        return int(n <= m)
    elif eq == "!":
        return int(n < m)